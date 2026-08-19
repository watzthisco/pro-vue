<script setup>
import Header from './components/Header.vue';
import Home from './components/Home.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div id="app">
    <Header />
    <Home />
    <Footer />
  </div>
</template>

<style>
h1 {
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  margin-bottom: 0;
}
.logo-font {
  vertical-align: middle;
}
.feed-toggle {
  margin-bottom: -1px;
}
</style>
