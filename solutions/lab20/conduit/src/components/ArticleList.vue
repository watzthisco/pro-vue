<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
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
  </div>
</template>
<script setup>
import ArticlePreview from './ArticlePreview.vue'
import { onMounted, ref, computed } from 'vue'
import { storeToRefs } from 'pinia'

import { useHomeStore } from '../stores/home'
import { useArticleFilter } from '../composables/useArticleFilter'
const props = defineProps({
  tag: { type: String, default: '' },
})
const articleFontSize = ref(1)
const homeStore = useHomeStore()
const { articles, isLoading } = storeToRefs(homeStore)
const { searchDetails, filterIt } = useArticleFilter(articles)
const visibleArticles = computed(() =>
  props.tag ? filterIt.value.filter((a) => (a.tagList ?? []).includes(props.tag)) : filterIt.value,
)

onMounted(() => {
  homeStore.fetchArticles({ type: 'all' })
})
</script>
