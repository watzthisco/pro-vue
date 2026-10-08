<script setup lang="ts">
import { onMounted, ref } from 'vue'
import MacroCounter from './components/MacroCounter.vue'

const count = ref(0)
const counter = ref<InstanceType<typeof MacroCounter> | null>(null)

onMounted(() => counter.value?.focusInput())
</script>

<template>
  <MacroCounter ref="counter" title="Counter" :count="count" @update-status="count += $event" />
</template>