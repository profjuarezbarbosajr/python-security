# Bcrypt is a password hashing function designed by Nelis Provos and David Mazières. 
# Bcrypt uses strong cryptography to hash and salts password based on the Blowfish cipher.

import bcrypt

# raw_input for pv2
user_raw = "juarez".encode("utf-8")
password_raw = "123123".encode("utf-8")

# function definition
def pass_thru_crypt(user, password):
           user_password = user + password
           hashed = bcrypt.hashpw(user_password, bcrypt.gensalt())
           if bcrypt.checkpw(user_password, hashed):
               print("Hello IBAT Cybersec Pros!")
           else:
               print("Oops...")

# function call
pass_thru_crypt(user_raw, password_raw)
