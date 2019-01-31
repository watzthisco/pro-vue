<template>
  <div id="app">
    <Header />
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Hello, World!"/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    Header,
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
