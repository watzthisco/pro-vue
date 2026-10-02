# Lab 19: Composables

A composable is a function that uses the Composition API to encapsulate and reuse stateful logic. Composables are what Vue 3 offers in place of mixins.

> **Note:** mixins still work in Vue 3, but the documentation marks them as legacy. Their problems are that the source of an inherited property is invisible at the point of use, that name collisions between mixins are resolved silently, and that a mixin cannot take parameters. A composable has none of these problems: you pass its inputs in and you name its outputs on the way out.

1. Make a directory inside `src` named `composables`.

2. Create a file in it named `useArticleFilter.js`.

   By convention a composable is named `use` followed by what it does, and lives in its own file.

3. Export a function that takes the list of articles as an argument and returns the search text and the filtered list.

   ```js
   import { computed, ref } from 'vue'

   export function useArticleFilter(articles) {
     const searchDetails = ref('')

     const filterIt = computed(() =>
       (articles.value ?? []).filter((article) =>
         article.title.includes(searchDetails.value),
       ),
     )

     return { searchDetails, filterIt }
   }
   ```

   Note that `articles` arrives as a ref, so the composable reads it through `.value` and stays reactive to changes made by the caller.

4. Use the composable in `ArticleList.vue`, and delete the local `searchDetails` ref and `filterIt` computed property.

   ```js
   import { useArticleFilter } from '../composables/useArticleFilter'

   const { searchDetails, filterIt } = useArticleFilter(articles)
   ```

5. Confirm the filter still works in the browser.

6. **Challenge:** implement filtering of the tags in the right column, reusing the same composable.
