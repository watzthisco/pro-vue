<script setup>
defineProps({
  msg: {
    type: String,
    default: '',
  },
});
</script>

<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <a href="https://vite.dev" target="_blank" rel="noopener">Vite documentation</a>.
    </p>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://discord.com/invite/vue" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://blog.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">Vue Router</a></li>
      <li><a href="https://pinia.vuejs.org" target="_blank" rel="noopener">Pinia</a></li>
      <li><a href="https://vitest.dev" target="_blank" rel="noopener">Vitest</a></li>
      <li><a href="https://devtools.vuejs.org" target="_blank" rel="noopener">Vue DevTools</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">Awesome Vue</a></li>
    </ul>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
