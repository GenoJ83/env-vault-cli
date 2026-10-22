# Architecture

```mermaid
flowchart LR
    Dotenv[.env file] --> Cipher[AES-256 Fernet]
    Key[Master Key] --> Cipher
    Cipher --> Vault[.env.vault]
```
