<script setup>
import { computed, ref } from 'vue';

const props = defineProps({
  article: { type: Object, required: true },
});

// ref() replaces the Options API `data()` function.
const favorited = ref(false);
const favoritesCount = ref(0);

const articleLink = computed(() => ({ slug: props.article.slug }));

function toggleFavorite() {
  favorited.value = !favorited.value;
  favoritesCount.value += 1;
}
</script>

<template>
  <div class="article-preview">
    <h1 v-text="article.title" />
    <button
      class="btn btn-sm float-end"
      :class="{
        'btn-primary': favorited,
        'btn-outline-primary': !favorited,
      }"
      @click="toggleFavorite"
    >
      <i class="ion-heart"></i>
      <span class="counter"> {{ favoritesCount }} </span>
    </button>
    <p v-text="article.description" />
    <span><a :href="articleLink.slug">Read more...</a></span>
  </div>
</template>
