<script setup>
import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';

import ArticlePreview from './ArticlePreview.vue';
import { useArticleFilter } from '../composables/useArticleFilter';
import { useHomeStore } from '../stores/home';

const homeStore = useHomeStore();
// State and getters need storeToRefs to stay reactive when destructured;
// actions can be pulled off the store directly.
const { articles, isLoading } = storeToRefs(homeStore);

const articleFontSize = ref(1);
const { searchDetails, filterIt } = useArticleFilter(articles);

onMounted(() => {
  homeStore.fetchArticles({ type: 'all' });
});
</script>

<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
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
  </div>
</template>
