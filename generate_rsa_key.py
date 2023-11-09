# PyCryptodome

# The following code generates a new RSA key pair (secret) and saves it into a file, 
# protected by a password. We use the scrypt key derivation function to thwart dictionary attacks. 
# At the end, the code prints our the RSA public key in ASCII/PEM format.

from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

file_out = open("ibat_rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

print(key.publickey().export_key())