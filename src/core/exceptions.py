class VaultError(Exception): pass
class DecryptionError(VaultError): pass
class MissingKeyError(VaultError): pass
