<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">No articles are here... yet.</div>
    <ArticlePreview
      v-for="(article, index) in articles"
      :key="article.title + index"
      :article="article"
      :style="{ fontSize: articleFontSize + 'em' }"
      @enlarge-text="articleFontSize += 0.1"
      @shrink-text="articleFontSize -= 0.1"
    />
  </div>
</template>
<script setup>
import ArticlePreview from './ArticlePreview.vue'
import { onMounted, ref } from 'vue';

import ApiService from '../common/api.service';

const articleFontSize = ref(1)
const articles = ref([])
async function fetchArticles() {
  const { data } = await ApiService.query('articles');

  return data.articles;
}
onMounted(async () => {
  articles.value = await fetchArticles();
});

</script>
