import { defineStore } from 'pinia';

import { ArticlesService } from '@/common/api.service';

// An "options store". It maps onto the Vuex module it replaces: state stays
// state, getters stay getters, and actions absorb what used to be split
// between actions and mutations -- Pinia has no mutations, so actions mutate
// state directly through `this`.
export const useHomeStore = defineStore('home', {
  state: () => ({
    tags: [],
    articles: [],
    isLoading: true,
    articlesCount: 0,
  }),

  actions: {
    async fetchArticles(params = {}) {
      this.isLoading = true;
      try {
        const { data } = await ArticlesService.query(params.type, params.filters);
        this.articles = data.articles;
        this.articlesCount = data.articlesCount;
      } finally {
        this.isLoading = false;
      }
    },

    setTags(tags) {
      this.tags = tags;
    },

    updateArticleInList(data) {
      this.articles = this.articles.map((article) =>
        article.slug === data.slug
          ? { ...article, favorited: data.favorited, favoritesCount: data.favoritesCount }
          : article,
      );
    },
  },
});
