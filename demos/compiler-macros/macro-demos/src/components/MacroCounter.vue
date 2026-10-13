<script setup lang="ts">
import { ref } from 'vue'
// Compiler macros such as defineProps and defineEmits are provided by Vue; do not import them.

interface Props {
  title: string
  count?: number
}

// defineProps declares the values this component accepts. withDefaults supplies
// a runtime default for the optional count prop.
const props = withDefaults(defineProps<Props>(), {
  count: 0
})

// defineEmits declares the event and its payload type. The parent can listen
// for "increment" and use the emitted number to update its own state.
const emit = defineEmits<{
  increment: [value: number]
}>()

// This named model is synced with the parent's v-model:active binding.
// Assigning to the ref emits update:active; receiving a parent update changes it.
const isActive = defineModel<boolean>('active', { default: false })

// defineOptions sets component metadata and options without a separate options object.
defineOptions({
  name: 'MacroCounter'
})

const buttonElement = ref<HTMLButtonElement | null>(null)

// Expose only this method so the parent can call it through a component ref.
const focusButton = () => {
  buttonElement.value?.focus()
}

defineExpose({
  focusButton
})
</script>

<template>
  <article class="macro-counter">
    <header>
      <p class="eyebrow">Child component</p>
      <h2>{{ props.title }}</h2>
      <p class="count">Parent's count: <strong>{{ props.count }}</strong></p>
    </header>

    <section class="example">
      <h3>defineProps + withDefaults</h3>
      <p>
        Props are read-only inputs from the parent. <code>count</code> is optional,
        so <code>withDefaults</code> would use 0 if the parent left it out.
      </p>
    </section>

    <section class="example">
      <h3>defineEmits</h3>
      <p>
        Clicking the button emits the next count. The parent listens for
        <code>increment</code> and stores that value.
      </p>
      <button ref="buttonElement" @click="emit('increment', props.count + 1)">
        Increment parent count
      </button>
    </section>

    <section class="example">
      <h3>defineModel</h3>
      <p>
        <code>isActive</code> is a two-way model: this button updates it, and the
        parent receives the same value through <code>v-model:active</code>.
      </p>
      <button
        type="button"
        :aria-pressed="isActive"
        @click="isActive = !isActive"
      >
        Turn {{ isActive ? 'off' : 'on' }}
      </button>
      <p class="model-state" aria-live="polite">
        Child model value: <strong>{{ isActive ? 'active' : 'inactive' }}</strong>
      </p>
    </section>

    <section class="example">
      <h3>defineOptions</h3>
      <p>
        Sets component options alongside <code>&lt;script setup&gt;</code>. Here,
        the component's name is <code>MacroCounter</code> in Vue DevTools.
      </p>
    </section>

    <section class="example">
      <h3>defineExpose</h3>
      <p>
        Script-setup components are private by default. This exposes
        <code>focusButton</code> so the parent can focus the increment button.
      </p>
    </section>
  </article>
</template>

<style scoped>
.macro-counter {
  display: grid;
  gap: 1rem;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: 0.75rem;
  background: var(--color-background-soft);
}

header {
  display: grid;
  gap: 0.25rem;
}

h2,
h3 {
  font-weight: 650;
}

h3 {
  font-size: 1rem;
}

.eyebrow {
  color: var(--color-heading);
  font-size: 0.75rem;
  font-weight: 650;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.count,
.model-state {
  margin-top: 0.25rem;
}

.example {
  display: grid;
  gap: 0.35rem;
}

button {
  justify-self: start;
  padding: 0.45rem 0.75rem;
  border: 1px solid var(--color-border-hover);
  border-radius: 0.4rem;
  color: var(--color-heading);
  background: var(--color-background);
  cursor: pointer;
}

button:focus-visible {
  outline: 3px solid hsla(160, 100%, 37%, 0.45);
  outline-offset: 2px;
}

code {
  padding: 0.05rem 0.25rem;
  border-radius: 0.2rem;
  background: var(--color-background-mute);
}
</style>
