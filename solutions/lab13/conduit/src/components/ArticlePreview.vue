<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="`/article/${article.slug}`">Read more...</a></span>
  </div>
</template>
<script setup>
defineProps({
  article: { type: Object, required: true },
})
</script>
