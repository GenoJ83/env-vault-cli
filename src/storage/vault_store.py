import os
def write_vault(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, 'w') as f: f.write(content)
