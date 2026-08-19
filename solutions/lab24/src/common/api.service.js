import axios from 'axios';

import JwtService from '@/common/jwt.service';
import { API_URL } from '@/common/config';

const client = axios.create({ baseURL: API_URL });

const ApiService = {
  init() {
    client.defaults.baseURL = API_URL;
  },

  setHeader() {
    client.defaults.headers.common.Authorization = `Token ${JwtService.getToken()}`;
  },

  query(resource, params) {
    return client.get(resource, params).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  get(resource, slug = '') {
    return client.get(`${resource}/${slug}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  post(resource, params) {
    return client.post(`${resource}`, params);
  },

  update(resource, slug, params) {
    return client.put(`${resource}/${slug}`, params);
  },

  put(resource, params) {
    return client.put(`${resource}`, params);
  },

  delete(resource) {
    return client.delete(resource).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
};

export default ApiService;

export const TagsService = {
  get() {
    return ApiService.get('tags');
  },
};

export const ArticlesService = {
  query(type, params) {
    return ApiService.query(`articles${type === 'feed' ? '/feed' : ''}`, {
      params,
    });
  },
  get(slug) {
    return ApiService.get('articles', slug);
  },
  create(params) {
    return ApiService.post('articles', { article: params });
  },
  update(slug, params) {
    return ApiService.update('articles', slug, { article: params });
  },
  destroy(slug) {
    return ApiService.delete(`articles/${slug}`);
  },
};

export const CommentsService = {
  get(slug) {
    if (typeof slug !== 'string') {
      throw new Error(
        '[RWV] CommentsService.get() article slug required to fetch comments',
      );
    }
    return ApiService.get('articles', `${slug}/comments`);
  },

  post(slug, payload) {
    return ApiService.post(`articles/${slug}/comments`, {
      comment: { body: payload },
    });
  },

  destroy(slug, commentId) {
    return ApiService.delete(`articles/${slug}/comments/${commentId}`);
  },
};

export const FavoriteService = {
  add(slug) {
    return ApiService.post(`articles/${slug}/favorite`);
  },
  remove(slug) {
    return ApiService.delete(`articles/${slug}/favorite`);
  },
};
