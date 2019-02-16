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
footer{
  background:#f3f3f3;
  margin-top:3rem;
  padding:1rem 0;
  position:absolute;
  bottom:0;
  width:100%
  }
footer .logo-font{
  vertical-align:middle
}
footer .attribution{
  vertical-align:middle;
  margin-left:10px;
  font-size:.8rem;
  color:#bbb;
  font-weight:300
  }
</style>