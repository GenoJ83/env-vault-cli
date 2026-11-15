from src.security.leak_detector import scan_plain_text_for_secrets
def test_leak_detection():
    assert scan_plain_text_for_secrets('API_KEY=ghp_secrettoken123')
    assert not scan_plain_text_for_secrets('APP_NAME=MyApp')
