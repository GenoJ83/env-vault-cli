import pytest
pytest.importorskip("cryptography")
from src.crypto.cipher import generate_key, encrypt_text, decrypt_text
def test_encrypt_decrypt_roundtrip():
    k = generate_key()
    cipher = encrypt_text('MY_SECRET_PW', k)
    plain = decrypt_text(cipher, k)
    assert plain == 'MY_SECRET_PW'
