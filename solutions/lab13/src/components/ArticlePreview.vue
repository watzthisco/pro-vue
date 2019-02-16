<template>
  <div class="article-preview">
      <h1 v-text="article.title" />
      <p v-text="article.description" />
      <span>Read more...</span>
  </div>
</template>

<script>
export default {
    name: 'ArticlePreview',
    props: {
    article: { type: Object, required: true }
    },
}
</script>
<style scoped>
.article-preview{
  border-top:1px solid rgba(0,0,0,.1);
  padding:1.5rem 0
  }
.article-preview .article-meta{
  margin:0 0 1rem
}
.article-preview .preview-link h1{
  font-weight:600;
  font-size:1.5rem;
  margin-bottom:3px
  }
.article-preview .preview-link p{
  font-weight:300;
  font-size:24px;
  color:#999;
  margin-bottom:15px;
  font-size:1rem;
  line-height:1.3rem
  }
.article-preview .preview-link span{
  max-width:30%;
  font-size:.8rem;
  font-weight:300;
  color:#bbb;
  vertical-align:middle
  }
.article-preview .preview-link ul{
  float:right;
  max-width:50%;
  vertical-align:top
  }
.article-preview .preview-link ul li{
  font-weight:300;
  font-size:.8rem;
  padding-top:0;
  padding-bottom:0;
  }
</style>