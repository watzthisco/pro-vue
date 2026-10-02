<script setup>
import ArticleList from './ArticleList.vue'

defineProps({
  tag: { type: String, default: '' },
})
</script>

<template>
  <div class="home-global"><ArticleList type="all" :tag="tag" /></div>
</template>
