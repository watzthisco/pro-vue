<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="`/article/${articleLink.slug}`">Read more...</a></span>
  </div>
</template>
<script setup>
import { computed } from 'vue'

const props = defineProps({
  article: { type: Object, required: true },
})

const articleLink = computed(() => ({ slug: props.article.slug }))
</script>
