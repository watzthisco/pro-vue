<template>
  <div>

      <div v-if="articles.length === 0" class="article-preview">
        No articles are here... yet.
      </div>
      <ArticlePreview
        :style="{ fontSize: articleFontSize + 'em' }"
        v-on:enlarge-text="articleFontSize += 0.1"
        v-for="(article, index) in articles"
        :article="article"
        :key="article.title + index"
      />
    </div>
</template>

<script>
import ArticlePreview from './ArticlePreview.vue';
import ApiService from "../common/api.service";

export default {
    name: 'ArticleList',
    components: {
    ArticlePreview
  },
  data(){
        return{
            articles: {},
            articleFontSize: 1
        }
  },
  async mounted() {
    let results = await this.fetchArticles();
    this.articles = results.data.articles;
    console.log(this.articles);
  },

  methods: {
    fetchArticles() {
      console.log("fetching articles");
      return ApiService.query("articles").catch(error => {
        throw new Error(`[RWV] ApiService ${error}`);
      });
    }
  }
}
</script>