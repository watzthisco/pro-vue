# Lab 20: Implementing Pinia

In this lab, you'll convert the Conduit application to use a centralized store with Pinia.

> **Note:** earlier versions of this course used Vuex. Vuex is now in maintenance mode and Pinia is the officially recommended store for Vue. The concepts carry over almost one for one: state and getters keep their names, and actions absorb what Vuex split between actions and mutations. Pinia has no mutations at all: an action assigns to state directly. It also drops the string action-type constants and the `dispatch`/`commit` indirection, so a store method is called like an ordinary function and can be type-checked and jumped to in an editor.

1. Install Pinia.

   ```bash
   npm install pinia
   ```

2. Import `createPinia` in `main.js` and install it on the app.

   ```js
   import { createApp } from 'vue'
   import { createPinia } from 'pinia'

   const app = createApp(App)

   app.use(createPinia())
   app.mount('#app')
   ```

   Unlike a Vuex store, a Pinia instance holds no state of its own. Each store is defined in its own file and registers itself the first time it is used.

3. Make a new directory in `src` named `stores`.

4. Make a new file, `home.js`, inside `stores`.

5. Make a new API service in `api.service.js` called `ArticlesService`.

   ```js
   export const ArticlesService = {
     query(type, params) {
       return ApiService.query(`articles${type === 'feed' ? '/feed' : ''}`, {
         params,
       })
     },
   }
   ```

6. Import `defineStore` and `ArticlesService` into `stores/home.js`.

   ```js
   import { defineStore } from 'pinia'

   import { ArticlesService } from '@/common/api.service'
   ```

7. Define and export the store. The first argument is a unique id; it is what the Vue DevTools label the store with.

   ```js
   export const useHomeStore = defineStore('home', {
   })
   ```

8. Add the state. As in a component, state is a function that returns a fresh object.

   ```js
   state: () => ({
     tags: [],
     articles: [],
     isLoading: true,
     articlesCount: 0,
   }),
   ```

   The Vuex version of this store also declared getters called `articles`, `isLoading`, `articlesCount` and `tags` that just returned the matching piece of state. In Pinia, state is exposed on the store directly, so those pass-through getters are unnecessary. Keep getters for values you actually derive.

9. Add the actions. An action can be `async`, and assigns to state through `this`; there is no commit and no mutation to write.

   ```js
   actions: {
     async fetchArticles(params = {}) {
       this.isLoading = true

       try {
         const { data } = await ArticlesService.query(
           params.type,
           params.filters,
         )

         this.articles = data.articles
         this.articlesCount = data.articlesCount
       } finally {
         this.isLoading = false
       }
     },
   },
   ```

   The `finally` block guarantees the loading flag is cleared even if the request fails, which the Vuex version did not do.

10. Add two more actions, `setTags` and `updateArticleInList`, replacing the mutations of the same names.

    ```js
    setTags(tags) {
      this.tags = tags
    },

    updateArticleInList(data) {
      this.articles = this.articles.map((article) =>
        article.slug === data.slug
          ? {
              ...article,
              favorited: data.favorited,
              favoritesCount: data.favoritesCount,
            }
          : article,
      )
    },
    ```

11. Import the store and `storeToRefs` into `ArticleList.vue`.

    ```js
    import { storeToRefs } from 'pinia'

    import { useHomeStore } from '../stores/home'
    ```

12. Call the store's composable and pull out the pieces you need.

    ```js
    const homeStore = useHomeStore()
    const { articles, isLoading } = storeToRefs(homeStore)
    ```

    > **Note:** a Pinia store is a reactive object, so destructuring it directly would break reactivity: you would copy the values out and never see an update. `storeToRefs` converts state and getters into refs that keep tracking. Actions are plain functions and can be destructured normally, or called on the store as we do below.

13. Remove the local `articles` ref from `ArticleList.vue`; the store owns that state now.

14. Change the `onMounted` hook to call the store action.

    ```js
    onMounted(() => {
      homeStore.fetchArticles({ type: 'all' })
    })
    ```

    Compare that with the Vuex version, which read `this.$store.dispatch(FETCH_ARTICLES, this.listConfig)` and needed a string constant and a computed property to build the payload.

15. Add a `v-if` directive to the `ArticleList` template to hide the list until the request has finished.

    ```vue
    <template>
      <div>
        <div v-if="isLoading" class="article-preview">Loading articles...</div>
        <div v-else>
          <input
            v-model="searchDetails"
            class="form-control"
            placeholder="filter articles"
          />
          <div v-if="articles.length === 0" class="article-preview">
            No articles are here... yet.
          </div>
          <ArticlePreview
            v-for="(article, index) in filterIt"
            :key="article.title + index"
            :style="{ fontSize: articleFontSize + 'em' }"
            :article="article"
            @enlarge-text="articleFontSize += 0.1"
          />
        </div>
      </div>
    </template>
    ```

16. Start the development server and view the app in a browser.

17. Open the Vue DevTools and find the Pinia tab. Watch `isLoading` flip as the request completes, and try editing articles directly from the inspector.

18. **Challenge:** display tags along with each article preview.

19. **Challenge:** populate the Popular Tags box with a list of tags from the currently displayed article previews.

20. **Challenge:** clicking on a tag in the list of popular tags should filter the display of articles.
