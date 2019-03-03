<template>
  <div class="article-preview">
      <h1 v-text="article.title" />
      <p v-text="article.description" />
      <span><a :href="articleLink.slug">Read more...</a></span>
  </div>
</template>

<script>
export default {
    name: 'ArticlePreview',
    props: {
      article: { type: Object, required: true }
    },
    computed: {
      articleLink() {
        return {
          slug: this.article.slug
        }
      }
    }
}
</script>