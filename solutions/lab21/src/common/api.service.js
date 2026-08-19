import axios from 'axios';

import { API_URL } from '@/common/config';

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

export const ArticlesService = {
  query(type, params) {
    return ApiService.query(`articles${type === 'feed' ? '/feed' : ''}`, {
      params,
    });
  },
};
