# PyCryptodome
# The following code encrypts a piece of data for a receiver we have the RSA public key of. 
# The RSA public key is stored in a file called receiver.pem.

# Since we want to be able to encrypt an arbitrary amount of data, we use a hybrid encryption scheme. 
# We use RSA with PKCS#1 OAEP for asymmetric encryption of an AES session key. The session key can then be
# used to encrypt all the actual data.

# As in the first example, we use the EAX mode to allow detection of unauthorized modifications.
# Since we want to be able to encrypt an arbitrary amount of data, we use a hybrid encryption scheme. 

# We use RSA with PKCS#1 OAEP for asymmetric encryption of an AES session key. 
# The session key can then be used to encrypt all the actual data.

# As in the first example, we use the EAX mode to allow detection of unauthorized modifications.

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

data = "I met aliens in UFO. Here is the map.".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
file_out.close()