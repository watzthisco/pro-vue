<script setup>
import { computed, onMounted, ref } from 'vue';

import ArticlePreview from './ArticlePreview.vue';
import ApiService from '../common/api.service';

const articles = ref([]);
const articleFontSize = ref(1);
const searchDetails = ref('');

// A computed property derived from two refs. It re-evaluates only when
// `articles` or `searchDetails` changes.
const filterIt = computed(() =>
  articles.value.filter((article) => article.title.includes(searchDetails.value)),
);

async function fetchArticles() {
  const { data } = await ApiService.query('articles');
  return data.articles;
}

onMounted(async () => {
  articles.value = await fetchArticles();
});
</script>

<template>
  <div>
    <input v-model="searchDetails" class="form-control" placeholder="filter articles" />
    <div v-if="articles.length === 0" class="article-preview">
      No articles are here... yet.
    </div>
    <ArticlePreview
      v-for="(article, index) in filterIt"
      :key="article.title + index"
      :style="{ fontSize: articleFontSize + 'em' }"
      :article="article"
      @enlarge-text="articleFontSize += 0.1"
    />
  </div>
</template>
