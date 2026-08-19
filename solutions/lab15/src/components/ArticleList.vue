<script setup>
import { ref } from 'vue';

import ArticlePreview from './ArticlePreview.vue';
import articlesJson from '../json/articles.json';

const articles = ref(articlesJson);
const articleFontSize = ref(1);
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
