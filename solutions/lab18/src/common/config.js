// The public RealWorld/Conduit demo API. Override it for a class by setting
// VITE_API_URL in a .env.local file at the project root.
export const API_URL = import.meta.env.VITE_API_URL ?? 'https://api.realworld.io/api';

export default API_URL;
