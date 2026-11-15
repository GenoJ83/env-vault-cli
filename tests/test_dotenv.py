from src.parsers.dotenv_parser import parse_dotenv
def test_parse_dotenv():
    raw = 'DATABASE_URL=postgres://localhost:5432/db\n# Comment\nDEBUG=true'
    d = parse_dotenv(raw)
    assert d['DATABASE_URL'] == 'postgres://localhost:5432/db'
    assert d['DEBUG'] == 'true'
