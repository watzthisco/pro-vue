<script setup>
import { RouterView } from 'vue-router';

import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div id="app">
    <Header />
    <RouterView />
    <Footer />
  </div>
</template>

<style></style>
