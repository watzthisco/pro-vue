<template>
  <div>

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
</template>

<script>
import ArticlePreview from './ArticlePreview.vue';
import articles from '../json/articles.json';

export default {
    name: 'ArticleList',
    components: {
    ArticlePreview
  },
  data(){
        return{
			    articleFontSize:1,
          articles: articles
        }
    }
}
</script>