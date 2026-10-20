<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">No articles are here... yet.</div>
    <ArticlePreview
      v-for="article in articles"
      :key="article.slug"
      :article="article"
    />
  </div>
</template>
<script setup>
import ArticlePreview from './ArticlePreview.vue'
import articlesJson from '../json/articles.json'

const articles = articlesJson.articles
</script>
