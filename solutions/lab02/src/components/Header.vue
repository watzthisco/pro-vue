<template>
  <div class="header">
    <nav>
      <span class="logo">Conduit</span>
      <ul>
        <li>Home</li>
        <li>Sign In</li>
        <li>Sign Up</li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .logo {
    float: left
  }
  ul {
      list-style-type: none;
      text-align: right;
      }
  li {
      display: inline;
      padding: 0 10px;
  }
</style>
