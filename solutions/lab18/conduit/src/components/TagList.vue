<template>
  <div class="sidebar">
    <p>Popular Tags</p>
    <ul class="tag-list">
      <slot>No tags available.</slot>
    </ul>
  </div>
</template>
<style scoped>
.sidebar {
  padding: 5px 10px 10px;
  background: #f3f3f3;
  border-radius: 4px;
}
ul {
  padding: 0;
  list-style: none;
}
</style>
