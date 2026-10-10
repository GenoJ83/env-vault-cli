import re
SECRET_PATTERNS = [re.compile(r'(?i)(api[_-]?key|secret|password|token)\s*=\s*["\']?[^\s"\']+')]
def scan_plain_text_for_secrets(text: str):
    return any(p.search(text) for p in SECRET_PATTERNS)
