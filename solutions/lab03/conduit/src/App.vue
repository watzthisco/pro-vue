<script setup>
import TheHeader from './components/TheHeader.vue'
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <TheHeader />
      <HelloWorld msg="Welcome to Pro Vue" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped></style>
