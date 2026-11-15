def format_secret_diff(old_keys: set, new_keys: set) -> str:
    added = new_keys - old_keys
    removed = old_keys - new_keys
    return f'Added keys: {list(added)}, Removed keys: {list(removed)}'
