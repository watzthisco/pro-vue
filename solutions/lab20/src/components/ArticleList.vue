<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
      <div v-if="articles.length === 0" class="article-preview">
        No articles are here... yet.
      </div>
      <ArticlePreview
        v-on:enlarge-text="articleFontSize += 0.1" 
        :style="{ fontSize: articleFontSize + 'em' }"
        v-for="(article, index) in articles"
        :article="article"
        :key="article.title + index"
      />
    </div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import ArticlePreview from './ArticlePreview.vue';
import { FETCH_ARTICLES } from "../store/actions.type";


export default {
    name: 'ArticleList',
    components: {
    ArticlePreview
  },

  data(){
      return{
        articleFontSize:1,
      }
  },
  computed: {
    listConfig() {
      const { type } = this;
      
      return {
        type,
      };
    },

  ...mapGetters(["articlesCount", "isLoading", "articles"]),
  },
  mounted() {
    this.fetchArticles();
  },
  
  methods: {
    fetchArticles() {
      this.$store.dispatch(FETCH_ARTICLES,this.listConfig);
    },

  }
}
</script>