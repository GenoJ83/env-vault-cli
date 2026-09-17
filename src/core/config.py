from pydantic import BaseModel
class VaultConfig(BaseModel):
    vault_dir: str = '.vault'
    key_env_var: str = 'ENV_VAULT_KEY'
    algorithm: str = 'AES-GCM'
