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
import { ref } from 'vue'
const articleFontSize = ref(1)
import articlesJson from '../json/articles.json'
const articles = ref(articlesJson)
</script>
