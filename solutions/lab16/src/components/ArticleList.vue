<script setup>
import { onMounted, ref } from 'vue';

import ArticlePreview from './ArticlePreview.vue';
import ApiService from '../common/api.service';

const articles = ref([]);
const articleFontSize = ref(1);

async function fetchArticles() {
  const { data } = await ApiService.query('articles');
  return data.articles;
}

// onMounted replaces the Options API `mounted` hook.
onMounted(async () => {
  articles.value = await fetchArticles();
});
</script>

<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">
      No articles are here... yet.
    </div>
    <ArticlePreview
      v-for="(article, index) in articles"
      :key="article.title + index"
      :style="{ fontSize: articleFontSize + 'em' }"
      :article="article"
      @enlarge-text="articleFontSize += 0.1"
    />
  </div>
</template>
