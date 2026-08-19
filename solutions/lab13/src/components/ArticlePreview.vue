<script setup>
import { computed } from 'vue';

const props = defineProps({
  article: { type: Object, required: true },
});

// A computed ref: recalculated only when `article` changes.
const articleLink = computed(() => ({ slug: props.article.slug }));
</script>

<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="articleLink.slug">Read more...</a></span>
  </div>
</template>
