<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
      <input
         class="form-control"
         v-model.number="searchDetails"
         placeholder="filter articles"
         >
      <div v-if="articles.length === 0" class="article-preview">
        No articles are here... yet.
      </div>
      <ArticlePreview
        :style="{ fontSize: articleFontSize + 'em' }"
        v-on:enlarge-text="articleFontSize += 0.1"
        v-for="(article, index) in filterIt"
        :article="article"
        :key="article.title + index"
      />
    </div>
    </div>
</template>

<script>
import ArticlePreview from './ArticlePreview.vue';
import ApiService from "../common/api.service";
import { mapGetters } from "vuex";
import { FETCH_ARTICLES } from "../store/actions.type";


export default {
    name: 'ArticleList',
    components: {
    ArticlePreview
  },
  data(){
    return{
      articleFontSize: 1,
      searchDetails: ''
    }
  },
  mounted() {
    this.fetchArticles();
  },

  computed: {
    filterIt: function(){
      var self = this;
      return this.articles.filter(function(a){
        return a.title.indexOf(self.searchDetails) > - 1
      }
      )
    },
    listConfig() {
      const { type } = this;
    
      return {
        type,
      };
    },
    ...mapGetters(["articlesCount", "isLoading", "articles"])
  },


  methods: {
    fetchArticles() {
      this.$store.dispatch(FETCH_ARTICLES,this.listConfig);
    },
  }
}
</script>