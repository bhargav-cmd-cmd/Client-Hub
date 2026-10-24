export function authError(error, fallback) {
  if (!error.response) return 'Cannot reach the account service. Start the local backend and try again.';
  const detail = error.response.data?.detail;
  if (typeof detail === 'string') return detail;
  if (Array.isArray(detail)) return detail.map(item => `${item.loc?.at(-1) || 'Input'}: ${item.msg}`).join('. ');
  return fallback;
}
