<template>
  <div class="home-page">
    <div class="banner">
      <div class="container">
        <h1 class="logo-font">conduit</h1>
        <p>A place to share your knowledge.</p>
      </div>
    </div>
    <div class="container page">
      <div class="row">
        <div class="col-md-9">
          <div class="feed-toggle">
            <ul class="nav nav-pills outline-active">
              <li class="nav-item">Global Feed</li>   
            </ul>
          </div>
        <GlobalFeed />
        </div>
        <div class="col-md-3">
          <div class="sidebar">
            <p>Popular Tags</p>
            <TagList />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import GlobalFeed from './GlobalFeed.vue';
import TagList from './TagList.vue';

export default {
    name: 'Home',
    components: {
      GlobalFeed,
      TagList
    }
}
</script>
<style scoped>
.banner {
  background:#5cb85c;
}
.banner p {
  color: #fff;
  text-align: center;
  font-size: 1.5rem;
  font-weight: 300;
}
.banner h1 {
  font-weight: 700;
  text-align: center;
  font-size: 3.5rem;
}
.sidebar {
  padding: 5px 10px 10px;
  background: #f3f3f3;
  border-radius: 4px;
}

</style>