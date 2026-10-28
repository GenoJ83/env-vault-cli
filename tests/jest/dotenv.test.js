const { parseDotenv } = require('../../js/dotenv');

describe('Dotenv Parser', () => {
  it('parses key-value pairs ignoring comments', () => {
    const raw = 'PORT=8080\n# DB\nDB_HOST=localhost';
    const env = parseDotenv(raw);
    expect(env.PORT).toBe('8080');
    expect(env.DB_HOST).toBe('localhost');
  });
  it('strips double and single quotes', () => {
    expect(parseDotenv('SECRET="secret_token"').SECRET).toBe('secret_token');
  });
});
