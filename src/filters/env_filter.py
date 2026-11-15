def filter_by_env(secrets: list, target_env: str):
    return [s for s in secrets if s.environment == target_env]
