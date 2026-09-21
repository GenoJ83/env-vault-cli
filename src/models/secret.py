from pydantic import BaseModel
class SecretEntry(BaseModel):
    key: str
    value: str
    environment: str = 'development'
