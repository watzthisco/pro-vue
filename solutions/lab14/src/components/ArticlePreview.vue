<template>
  <div class="article-preview">
      <h1 v-text="article.title" />
      <button
        class="btn btn-sm float-right"
        v-on:click="toggleFavorite"
        :class="{
          'btn-primary': favorited,
          'btn-outline-primary': !favorited
        }"
      >
        <i class="ion-heart"></i>
      </button>
      <p v-text="article.description" />
      <span><a :href="articleLink.slug">Read more...</a></span>
  </div>
</template>

<script>
export default {
    name: 'ArticlePreview',
    data: function(){
      return {
        favorited: false
      }
    },
    props: {
      article: { type: Object, required: true }
    },
    computed: {
      articleLink() {
        return {
          slug: this.article.slug
        }
      }
    },
    methods: {
      toggleFavorite() {
        this.favorited = !this.favorited;
        console.log("favorited = " + this.favorited);

      }
    }
}
</script>