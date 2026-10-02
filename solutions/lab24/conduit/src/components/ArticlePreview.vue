<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="`/article/${articleLink.slug}`">Read more...</a></span>
    <slot name="tags" />
    <button @click="emit('enlarge-text', 0.1)">Enlarge Text</button>
    <button @click="emit('shrink-text', 0.1)">Shrink Text</button>
    <button class="btn btn-sm float-end ms-1" aria-label="Remove from feed" @click="emit('remove')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path
          d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0zM14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"
        />
      </svg>
    </button>
    <button
      class="btn btn-sm float-end"
      :class="{
        'btn-primary': favorited,
        'btn-outline-primary': !favorited,
      }"
      @click="toggleFavorite"
    >
      <i class="ion-heart"></i> {{ favoritesCount }}
    </button>
  </div>
</template>
<script setup>
import { computed } from 'vue'
import { ref } from 'vue'

const favorited = ref(false)
const favoritesCount = ref(0)
const emit = defineEmits(['enlarge-text', 'shrink-text', 'remove'])

const props = defineProps({
  article: { type: Object, required: true },
})

function toggleFavorite() {
  favorited.value = !favorited.value
  favoritesCount.value++
}

const articleLink = computed(() => ({ slug: props.article.slug }))
</script>
