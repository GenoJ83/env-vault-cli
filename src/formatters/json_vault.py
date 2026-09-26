import json
def export_vault_json(encrypted_data: dict) -> str:
    return json.dumps({'version': 1, 'data': encrypted_data}, indent=2)
