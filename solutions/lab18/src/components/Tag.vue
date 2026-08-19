<script setup>
defineProps({
  tag: { type: String, required: true },
});
</script>

<template>
  <li class="tag-default tag-pill tag-outline">{{ tag }}</li>
</template>
