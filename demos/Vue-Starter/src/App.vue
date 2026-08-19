<script setup>
import { ref } from 'vue';

const message = ref('Hello World');
</script>

<template>
  <div id="app">
    {{ message }}
  </div>
</template>

<style>
#app {
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: blue;
}
</style>
