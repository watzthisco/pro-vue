<template>
  <div id="app">
    <Header />
    <Home />
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header';
import Home from './components/Home';
import Footer from './components/Footer';

export default {
  name: 'app',
  components: {
    Header,
    Home,
    Footer
  }
}
</script>

<style>
h1{
  text-shadow:0 1px 3px rgba(0,0,0,.3);
  margin-bottom:0;
  }
.logo-font {
  vertical-align:middle;
  }
.feed-toggle{
  margin-bottom:-1px;
  }

</style>
