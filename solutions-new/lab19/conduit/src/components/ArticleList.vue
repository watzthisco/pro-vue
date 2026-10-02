<template>
  <div>
    <div v-if="articles.length === 0" class="article-preview">No articles are here... yet.</div>
    <input v-model="searchDetails" class="form-control" placeholder="filter articles" />

    <ArticlePreview
      v-for="(article, index) in visibleArticles"
      :key="article.title + index"
      :article="article"
      :style="{ fontSize: articleFontSize + 'em' }"
      @enlarge-text="articleFontSize += 0.1"
      @shrink-text="articleFontSize -= 0.1"
    >
      <template #tags>
        <ul class="tag-list">
          <li v-for="t in article.tagList" :key="t" class="tag-default tag-pill tag-outline">
            {{ t }}
          </li>
        </ul>
      </template>
    </ArticlePreview>
  </div>
</template>
<script setup>
import ArticlePreview from './ArticlePreview.vue'
import { onMounted, ref, computed } from 'vue'

import ApiService from '../common/api.service'
import { useArticleFilter } from '../composables/useArticleFilter'
const props = defineProps({
  tag: { type: String, default: '' },
})
const articleFontSize = ref(1)
const articles = ref([])
const { searchDetails, filterIt } = useArticleFilter(articles)
const visibleArticles = computed(() =>
  props.tag ? filterIt.value.filter((a) => (a.tagList ?? []).includes(props.tag)) : filterIt.value,
)

async function fetchArticles() {
  const { data } = await ApiService.query('articles')

  return data.articles
}
onMounted(async () => {
  articles.value = await fetchArticles()
})
</script>
