# Quantum-Safe Cryptography

**Quantum computers** come with significant advancements in computing power, post-quantum threats are becoming very real. Some security experts believe Q-Day will occur within the next decade, potentially leaving all digital information vulnerable under current encryption protocols. The point at which quantum computers can break existing cryptographic algorithms such as public-key cryptography (PKC) - known as "Q-Day" - is approaching. 

RSA, an encryption scheme that allows systems to share keys, could take a classical computer most of the lifetime of the Universe to reverse-engineer. A quantum computer, researchers estimate, could do the same job in 8 hours. The Diffie–Hellman key exchange, another widely used cryptographic method named after its two inventors, could also be easily reversed by a quantum machine. A different type of scheme, the Advanced Encryption Standard, is not considered to be under serious threat by computational advances. However, it's often used with other methods and can't replace their secret-keeping abilities.

**Quantum computing** is a model of computing based on the quantum physics, which works differently than classical computers and can do things that classical computers can’t, such  
as breaking RSA and ECC efficiently. **Quantum computers** are not "faster computers" and they are not all-powerful and cannot do any computing job faster. Quantum computers are very efficient for certain problems and quite weak for others.

It is well known in computer science that **quantum computers will break some cryptographic algorithms**, especially the public-key cryptosystems like **RSA**, **ECC** and **ECDSA** that rely on the **IFP** \(integer factorization problem\), the **DLP** \(discrete logarithms problem\) and the **ECDLP** \(elliptic-curve discrete logarithm problem\). Quantum algorithms will not be the end of cryptography, because:

* Only some cryptosystems are **quantum-unsafe** \(like RSA, DHKE, ECC, ECDSA and ECDH\).
* Some cryptosystems are **quantum-safe** and will be only slightly affected \(like cryptographic hashes, MAC algorithms and symmetric key ciphers\).

## Quantum-Safe and Quantum-Broken Crypto Algorithms

Most cryptographic **hashes** \(like SHA2, SHA3, BLAKE2\), **MAC** algorithms \(like HMAC and CMAK\), **key-derivation functions** \(bcrypt, Scrypt, Argon2\) are basically **quantum-safe** \(only slightly affected by quantum computing\).

* Use 384-bits or more to be quantum-safe \(256-bits should be enough for long time\)

**Symmetric ciphers** \(like AES-256, Twofish-256\) are **quantum-safe**.

* Use 256-bits or more as key length \(don't use 128-bit AES\)

Most popular **public-key cryptosystems** \(like RSA, DSA, ECDSA, EdDSA, DHKE, ECDH, ElGamal\) are **quantum-broken**!

* Most **digital signature** algorithms \(like RSA, ECDSA, EdDSA\) are **quantum-broken**!
* **Quantum-safe signature** algorithms and public-key cryptosystems are already developed \(e.g. lattice-based or hash-based signatures\), but are not massively used, because of longer keys and longer signatures than ECC.

See [https://en.wikipedia.org/wiki/Post-quantum\_cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography)

### ECC Cryptography and Most Digital Signatures are Quantum-Broken!

A **k**-bit number can be factored in time of order **O\(k^3\)** using a quantum computer of **5k+1 qubits** \(using Shor's algorithm\).

* See [http://www.theory.caltech.edu/~preskill/pubs/preskill-1996-networks.pdf](http://www.theory.caltech.edu/~preskill/pubs/preskill-1996-networks.pdf)

256-bit number \(e.g. Bitcoin public key\) can be factorized using 1281 qubits in 72\*256^3 quantum operations.

* ~ 1.2 billion operations == ~ less than 1 second using good machine

ECDSA, DSA, RSA, ElGamal, DHKE, ECDH cryptosystems are all quantum-broken

Conclusion: publishing the signed transactions \(like Ethereum does\) is not quantum safe -&gt; avoid revealing the ECC public key

### Hashes are Quantum Safe

Cryptographic **hashes** \(like SHA2, SHA3, BLAKE2\) are considered **quantum-safe**:

* On traditional computer, finding a collision for 256-bit hash takes √2^256 steps \(using the [**birthday attack**](https://en.wikipedia.org/wiki/Birthday_attack)\) -&gt; SHA256 has 2^128 crypto-strength
* Quantum computers might find hash collisions in ∛2^256 operations \(see [the BHT algorithm](https://arxiv.org/pdf/quant-ph/9705002.pdf)\), but this is disputed \(see \[Bernstein 2009\] - [http://cr.yp.to/hash/collisioncost-20090823.pdf](http://cr.yp.to/hash/collisioncost-20090823.pdf)
* On theory it might take 2^85 quantum operations to find SHA256 / SHA3-256 collision, but in practice it may cost significantly more. 

Conclusion: SHA256 / SHA3-256 are most probably quantum-safe

* SHA384, SHA512 and SHA3-384, SHA3-512 are quantum-safe

### Symmetric Ciphers are Quantum Safe

Most symmetric ciphers \(like AES and ChaCha20\) are quantum-safe:

* Grover's algorithm [https://en.wikipedia.org/wiki/Grover%27s_algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm)
* Quantum era will **double the key size** of the symmetric ciphers, see [http://cr.yp.to/codes/grovercode-20100303.pdf](http://cr.yp.to/codes/grovercode-20100303.pdf%29%29\)

AES-256 in the post-quantum era is like AES-128 before

* 128-bits or less symmetric ciphers are quantum-attackable

Conclusion: 256-bit symmetric ciphers are generally quantum safe

* AES-256, ChaCha20-256, Twofish-256, Camellia-256 are considered quantum-safe

## Post-Quantum Cryptography

Quantum-Safe key agreement: [https://en.wikipedia.org/wiki/CECPQ1](https://en.wikipedia.org/wiki/CECPQ1)

[https://ianix.com/pqcrypto/pqcrypto-deployment.html](https://ianix.com/pqcrypto/pqcrypto-deployment.html)

[https://pqcrypto.org](https://pqcrypto.org/)

Post-quantum signature scheme XMSS:

* [https://tools.ietf.org/html/rfc8391](https://legacy.gitbook.com/book/svetlin-nakov/practical-cryptography-for-developers/edit#)
* JS XMSS - [https://www.npmjs.com/package/xmss](https://www.npmjs.com/package/xmss)
* Post-quantum key agreement schemes McEliece and NewHope

Post-quantum signatures and key agreements \(XMSS, McEliece, NewHope\):  
[https://github.com/randombit/botan](https://github.com/randombit/botan)

QC-MDPC and libPQC are quantum-broken: [https://eprint.iacr.org/2016/858.pdf](https://eprint.iacr.org/2016/858.pdf)

## Quantum-Resistant Cryptography - Libraries

The quantum-safe cryptography is still emerging, not mature, and still not widely supported by the most crypto-libraries and tools like Web browsers, OpenSSL, OpenSSH, etc. This is a list of well developed quantum crypto algorithm libraries:

* **liboqs** \(Open Quantum Safe\) - [https://github.com/open-quantum-safe/liboqs](https://github.com/open-quantum-safe/liboqs)
* **Bouncy Castle PQC** - [https://github.com/bcgit/bc-java/tree/master/core/src/main/java/org/bouncycastle/pqc/crypto](https://github.com/bcgit/bc-java/tree/master/core/src/main/java/org/bouncycastle/pqc/crypto)
