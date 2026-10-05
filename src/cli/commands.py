from src.crypto.cipher import generate_key
def cmd_init():
    key = generate_key()
    print(f'New Vault Key Generated: {key}')
    return key
