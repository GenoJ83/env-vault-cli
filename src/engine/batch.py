from src.crypto.cipher import encrypt_text
def encrypt_dict(data: dict, key: str) -> dict:
    return {k: encrypt_text(v, key) for k, v in data.items()}
