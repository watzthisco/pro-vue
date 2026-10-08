<script setup lang="ts">
import { ref } from 'vue'
// ❌ DO NOT IMPORT compiler macros like defineProps or defineEmits

// 1. Props with default values
interface Props {
  title: string
  count?: number
}
const props = withDefaults(defineProps<Props>(), {
  count: 0
})

// 2. Component events
const emit = defineEmits<{
  (e: 'updateStatus', id: number): void
}>()

// 3. Two-way binding v-model (Vue 3.4+)
const isActive = defineModel<boolean>({ default: false })

// 4. Declaring component options
defineOptions({
  name: 'CustomButton',
  inheritAttrs: false
})

// 5. Exposing specific methods to parents
const buttonElement = ref<HTMLButtonElement | null>(null)

const focusInput = () => {
  buttonElement.value?.focus()
}

defineExpose({
  focusInput
})
</script>

<template>
  <div>
    <h1>{{ title }} ({{ count }})</h1>
    <button ref="buttonElement" @click="emit('updateStatus', 1)">Update</button>
  </div>
</template>
