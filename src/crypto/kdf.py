import os, hashlib
def derive_key(passphrase: str, salt: bytes = None):
    salt = salt or os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), salt, 100000)
    return key, salt
