def parse_dotenv(content: str) -> dict:
    res = {}
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            res[k.strip()] = v.strip().strip('"\'')
    return res
