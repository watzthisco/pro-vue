<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
      <div v-if="articles.length === 0" class="article-preview">No articles are here... yet.</div>
      <input v-model="searchDetails" class="form-control" placeholder="filter articles" />

      <TransitionGroup name="article" tag="div" class="article-list">
        <ArticlePreview
          v-for="article in visibleArticles"
          :key="article.slug"
          :article="article"
          :style="{ fontSize: articleFontSize + 'em' }"
          @enlarge-text="articleFontSize += 0.1"
          @shrink-text="articleFontSize -= 0.1"
          @remove="homeStore.removeArticle(article.slug)"
        >
          <template #tags>
            <ul class="tag-list">
              <li v-for="t in article.tagList" :key="t" class="tag-default tag-pill tag-outline">
                {{ t }}
              </li>
            </ul>
          </template>
        </ArticlePreview>
      </TransitionGroup>
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
  sortBy: { type: String, default: '' },
})
const articleFontSize = ref(1)
const homeStore = useHomeStore()
const { articles, isLoading } = storeToRefs(homeStore)
const { searchDetails, filterIt } = useArticleFilter(articles)
const visibleArticles = computed(() => {
  const list = props.tag
    ? filterIt.value.filter((a) => (a.tagList ?? []).includes(props.tag))
    : filterIt.value
  return props.sortBy ? [...list].sort((a, b) => b[props.sortBy] - a[props.sortBy]) : list
})

onMounted(() => {
  homeStore.fetchArticles({ type: 'all' })
})
</script>
<style scoped>
.article-list {
  position: relative;
}

.article-enter-from,
.article-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.article-enter-active,
.article-leave-active {
  transition: all 0.3s ease;
}

/* Take leaving items out of flow so .article-move can slide the rest up. */
.article-leave-active {
  position: absolute;
  width: 100%;
}

.article-move {
  transition: transform 0.3s ease;
}
</style>
