<template>
  <footer>
    <div class="container">
	conduit
      <span class="attribution">
		Code &amp; design licensed under MIT.
      </span>
    </div>
  </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>
<style scoped>

footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  /* Set the fixed height of the footer here */
  height: 60px;
  line-height: 60px; /* Vertically center the text there */
  background-color: #f5f5f5;
}
</style>