<script setup>
import ArticleList from './ArticleList.vue'

defineProps({
  tag: { type: String, default: '' },
})
</script>

<template>
  <div class="home-popular"><ArticleList type="all" :tag="tag" sort-by="favoritesCount" /></div>
</template>
