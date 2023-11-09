# PyCryptodome
# The following code generates public key stored in receiver.pem and private key stored in private.pem. 
# These files will be used in the examples below. Every time, it generates different public key and private key pair.

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()