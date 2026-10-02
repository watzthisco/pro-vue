<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <p v-text="article.description" />
    <span><a :href="`/article/${articleLink.slug}`">Read more...</a></span>
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

const props = defineProps({
  article: { type: Object, required: true },
})

function toggleFavorite() {
  favorited.value = !favorited.value
  favoritesCount.value++
}

const articleLink = computed(() => ({ slug: props.article.slug }))
</script>
