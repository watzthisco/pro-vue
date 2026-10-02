<template>
  <li class="tag-default tag-pill tag-outline" :class="{ active }" @click="emit('select', tag)">
    {{ tag }}
  </li>
</template>
<script setup>
defineProps({
  tag: { type: String, required: true },
  active: { type: Boolean, default: false },
})
const emit = defineEmits(['select'])
</script>
<style scoped>
li {
  cursor: pointer;
  display: inline-block;
  margin-right: 4px;
}
.active {
  background: #5cb85c;
  color: #fff;
}
</style>
