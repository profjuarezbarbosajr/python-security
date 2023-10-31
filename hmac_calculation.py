import hashlib, hmac, binascii

def hmac_sha256(key_arg, msg_arg):
    return hmac.new(key_arg, msg_arg, hashlib.sha256).digest()

key = b"12345"
msg = b"sample message"
print(binascii.hexlify(hmac_sha256(key, msg)))