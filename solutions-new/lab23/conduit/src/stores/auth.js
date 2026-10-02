import { defineStore } from 'pinia';

import ApiService from '@/common/api.service';
import JwtService from '@/common/jwt.service';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    errors: null,
    user: {},
    isAuthenticated: !!JwtService.getToken(),
  }),

  getters: {
    currentUser: (state) => state.user,
  },

  actions: {
    setAuth(user) {
      this.isAuthenticated = true;
      this.user = user;
      this.errors = {};
      JwtService.saveToken(user.token);
    },

    purgeAuth() {
      this.isAuthenticated = false;
      this.user = {};
      this.errors = {};
      JwtService.destroyToken();
    },

    async login(credentials) {
      try {
        const { data } = await ApiService.post('users/login', { user: credentials });
        this.setAuth(data.user);
        return data;
      } catch (error) {
        this.errors = error.response?.data?.errors ?? { error: [error.message] };
        throw error;
      }
    },

    logout() {
      this.purgeAuth();
    },

    async register(credentials) {
      try {
        const { data } = await ApiService.post('users', { user: credentials });
        this.setAuth(data.user);
        return data;
      } catch (error) {
        this.errors = error.response?.data?.errors ?? { error: [error.message] };
        throw error;
      }
    },

    async checkAuth() {
      if (!JwtService.getToken()) {
        this.purgeAuth();
        return;
      }
      ApiService.setHeader();
      try {
        const { data } = await ApiService.get('user');
        this.setAuth(data.user);
      } catch (error) {
        this.errors = error.response?.data?.errors ?? { error: [error.message] };
      }
    },

    async updateUser({ email, username, password, image, bio }) {
      const user = { email, username, bio, image };
      if (password) {
        user.password = password;
      }
      const { data } = await ApiService.put('user', user);
      this.setAuth(data.user);
      return data;
    },
  },
});
