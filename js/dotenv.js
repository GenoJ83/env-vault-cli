function parseDotenv(content) {
  const env = {};
  if (!content) return env;
  const lines = content.split('\n');
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue;
    const [key, ...vals] = trimmed.split('=');
    let val = vals.join('=').trim().replace(/^["']|["']$/g, '');
    env[key.trim()] = val;
  }
  return env;
}
module.exports = { parseDotenv };
