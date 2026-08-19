<script setup>
defineProps({
  article: { type: Object, required: true },
});
</script>

<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span>Read more...</span>
  </div>
</template>
