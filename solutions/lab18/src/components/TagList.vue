<script setup>
import { onMounted, ref } from 'vue';

import Tag from './Tag.vue';
import ApiService from '../common/api.service';

const tags = ref([]);

async function fetchTags() {
  const { data } = await ApiService.query('tags');
  return data.tags;
}

onMounted(async () => {
  tags.value = await fetchTags();
});
</script>

<template>
  <div class="tag-list">
    <div v-if="tags.length === 0">No Tags are here... yet.</div>
    <ul class="tag-list">
      <Tag v-for="(tag, index) in tags" :key="tag + index" :tag="tag" />
    </ul>
  </div>
</template>
