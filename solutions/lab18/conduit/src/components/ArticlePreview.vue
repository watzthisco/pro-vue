<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="`/article/${articleLink.slug}`">Read more...</a></span>
    <slot name="tags" />
    <button @click="emit('enlarge-text', 0.1)">Enlarge Text</button>
    <button @click="emit('shrink-text', 0.1)">Shrink Text</button>
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
const emit = defineEmits(['enlarge-text', 'shrink-text'])

const props = defineProps({
  article: { type: Object, required: true },
})

function toggleFavorite() {
  favorited.value = !favorited.value
  favoritesCount.value++
}

const articleLink = computed(() => ({ slug: props.article.slug }))
</script>
