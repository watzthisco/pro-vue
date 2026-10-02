<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">No articles are here... yet.</div>
    <input v-model="searchDetails" class="form-control" placeholder="filter articles" />

    <ArticlePreview
      v-for="(article, index) in filterIt"
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
import { onMounted, ref, computed } from 'vue'

import ApiService from '../common/api.service'
const searchDetails = ref('')
const articleFontSize = ref(1)
const articles = ref([])
const filterIt = computed(() => {
  const term = searchDetails.value.toLowerCase()
  return articles.value.filter(
    (article) =>
      article.title.toLowerCase().includes(term) ||
      (article.description ?? '').toLowerCase().includes(term),
  )
})

async function fetchArticles() {
  const { data } = await ApiService.query('articles')

  return data.articles
}
onMounted(async () => {
  articles.value = await fetchArticles()
})
</script>
