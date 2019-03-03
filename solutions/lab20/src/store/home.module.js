import { FETCH_ARTICLES } from "./actions.type";
import {
    FETCH_START,
    FETCH_END,
    SET_TAGS,
    UPDATE_ARTICLE_IN_LIST
  } from "./mutations.type";

import { ArticlesService } from "@/common/api.service";
const state = {
    tags: [],
    articles: [],
    isLoading: true,
    articlesCount: 0
  };
const getters = {
articlesCount(state) {
    return state.articlesCount;
},
articles(state) {
    return state.articles;
},
isLoading(state) {
    return state.isLoading;
},
tags(state) {
    return state.tags;
}
};
const actions = {
[FETCH_ARTICLES]({ commit }, params) {
    commit(FETCH_START);
    return ArticlesService.query(params.type, params.filters)
    .then(({ data }) => {
        commit(FETCH_END, data);
    })
    .catch(error => {
        throw new Error(error);
    });
},
};  
const mutations = {
[FETCH_START](state) {
    state.isLoading = true;
},
[FETCH_END](state, { articles, articlesCount }) {
    state.articles = articles;
    state.articlesCount = articlesCount;
    state.isLoading = false;
},
[SET_TAGS](state, tags) {
    state.tags = tags;
},
[UPDATE_ARTICLE_IN_LIST](state, data) {
    state.articles = state.articles.map(article => {
    if (article.slug !== data.slug) {
        return article;
    }
    
    article.favorited = data.favorited;
    article.favoritesCount = data.favoritesCount;
    return article;
    });
}
};
  
export default {
    state,
    getters,
    actions,
    mutations
  };
  