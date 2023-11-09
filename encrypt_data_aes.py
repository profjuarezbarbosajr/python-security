# PyCryptodome

# The following code generates a new AES128 key and encrypts a piece of data into a file. 
# We use the EAX mode because it allows the receiver to detect any unauthorized modification (similarly, 
# we could have used other authenticated encryption modes like GCM, CCM or SIV).

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()