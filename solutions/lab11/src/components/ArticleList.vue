<script setup>
import { ref } from 'vue';

import ArticlePreview from './ArticlePreview.vue';
import articlesJson from '../json/articles.json';

const articles = ref(articlesJson);
</script>

<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">
      No articles are here... yet.
    </div>
    <ArticlePreview
      v-for="(article, index) in articles"
      :key="article.title + index"
      :article="article"
    />
  </div>
</template>
