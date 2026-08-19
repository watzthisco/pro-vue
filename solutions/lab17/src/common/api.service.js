import axios from 'axios';

import { API_URL } from '@/common/config';

// Vue 3 has no global `Vue` object to hang axios off, so we create a
// configured axios instance and export the service that wraps it.
const client = axios.create({ baseURL: API_URL });

const ApiService = {
  init() {
    client.defaults.baseURL = API_URL;
  },

  query(resource, params) {
    return client.get(resource, params).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
};

export default ApiService;
