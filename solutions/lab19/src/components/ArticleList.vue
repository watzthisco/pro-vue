<script setup>
import { onMounted, ref } from 'vue';

import ArticlePreview from './ArticlePreview.vue';
import ApiService from '../common/api.service';
import { useArticleFilter } from '../composables/useArticleFilter';

const articles = ref([]);
const articleFontSize = ref(1);

// Composables are the Composition API's replacement for mixins: the state
// a composable uses is passed in and returned explicitly, so there is no
// hidden merging of options and no name collisions.
const { searchDetails, filterIt } = useArticleFilter(articles);

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
