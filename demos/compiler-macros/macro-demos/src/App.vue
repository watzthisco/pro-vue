<script setup lang="ts">
import { onMounted, ref } from 'vue'
import MacroCounter from './components/MacroCounter.vue'

const count = ref(0)
const isActive = ref(false)
const counter = ref<InstanceType<typeof MacroCounter> | null>(null)

onMounted(() => counter.value?.focusButton())
</script>

<template>
  <main>
    <header class="page-header">
      <p class="eyebrow">Vue 3 · &lt;script setup&gt;</p>
      <h1>Compiler macros</h1>
      <p>
        Macros declare component props, events, models, options, and public
        methods. Vue processes them at compile time, so they are not imported
        from <code>vue</code>.
      </p>
    </header>

    <section class="parent-state" aria-live="polite">
      <h2>Parent component state</h2>
      <p>Count received from child event: <strong>{{ count }}</strong></p>
      <p>
        Active model received from child:
        <strong>{{ isActive ? 'active' : 'inactive' }}</strong>
      </p>
      <button type="button" @click="counter?.focusButton()">
        Focus the child's increment button
      </button>
      <p class="usage">
        The parent passes <code>title</code> and <code>count</code>, handles
        <code>@increment</code>, syncs <code>v-model:active</code>, and calls the
        exposed method through <code>ref</code>.
      </p>
    </section>

    <MacroCounter
      ref="counter"
      title="Macro counter"
      :count="count"
      v-model:active="isActive"
      @increment="count = $event"
    />
  </main>
</template>

<style scoped>
:global(body) {
  display: block;
}

:global(#app) {
  display: block;
  width: min(100%, 900px);
  max-width: 900px;
  padding: 2rem;
}

main {
  display: grid;
  gap: 1.5rem;
}

.page-header {
  display: grid;
  gap: 0.6rem;
}

h1,
h2 {
  font-weight: 700;
}

h1 {
  font-size: clamp(2rem, 6vw, 3rem);
  line-height: 1.1;
}

h2 {
  font-size: 1.15rem;
}

.eyebrow {
  color: var(--color-heading);
  font-size: 0.75rem;
  font-weight: 650;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.parent-state {
  display: grid;
  gap: 0.35rem;
  padding: 1.25rem;
  border-left: 4px solid hsla(160, 100%, 37%, 1);
  background: var(--color-background-soft);
}

.parent-state button {
  justify-self: start;
  margin-top: 0.35rem;
  padding: 0.45rem 0.75rem;
  border: 1px solid var(--color-border-hover);
  border-radius: 0.4rem;
  color: var(--color-heading);
  background: var(--color-background);
  cursor: pointer;
}

.parent-state button:focus-visible {
  outline: 3px solid hsla(160, 100%, 37%, 0.45);
  outline-offset: 2px;
}

.usage {
  margin-top: 0.35rem;
}

code {
  padding: 0.05rem 0.25rem;
  border-radius: 0.2rem;
  background: var(--color-background-mute);
}
</style>