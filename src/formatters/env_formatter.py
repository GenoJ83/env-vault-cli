def format_as_dotenv(data: dict) -> str:
    return '\n'.join(f'{k}={v}' for k, v in sorted(data.items())) + '\n'
