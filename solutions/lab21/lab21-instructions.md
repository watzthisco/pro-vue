# Lab 21: Routing

So far, our application only has one screen. In this lab, you'll start to implement additional routes. Routing in modern JavaScript frameworks works by reacting to changes in the browser address to load or show different views. In reality everything is happening in the same HTML page, but the data and view change. This is what we mean by a Single Page Application (or SPA).

In this lab, you'll install and configure Vue Router, and then create the first two additional routes for this application: Sign In and Sign Up.

1. Install `vue-router`.

   ```bash
   npm install vue-router
   ```

2. Make a new directory in `src` named `router`.

3. Create a file named `index.js` inside `src/router`.

4. Import the router factory functions. Vue Router 4 and later are created with a function rather than a constructor, and are not installed with `Vue.use`.

   ```js
   import { createRouter, createWebHistory } from 'vue-router'
   ```

   > **Note:** this is the biggest API change from Vue Router 3. `new Router()` becomes `createRouter()`; the `mode: 'history'` option becomes `createWebHistory()`; `mode: 'hash'` becomes `createWebHashHistory()`; and the catch-all path `*` becomes `/:pathMatch(.*)*`.

5. Create and export the router, passing it a history implementation and a `routes` array.

   ```js
   export default createRouter({
     history: createWebHistory(import.meta.env.BASE_URL),
     routes: [],
   })
   ```

   `createWebHistory` uses the HTML5 History API, so URLs have no `#`. That is why the `/#/` you may have seen in older versions of this app is gone.

6. Make the first (default) route. Remember the `.vue` extension in the dynamic import.

   ```js
   routes: [
     {
       name: 'home',
       path: '/',
       component: () => import('@/components/HomeContent.vue'),
     },
   ],
   ```

   Writing the component as an arrow function that returns an `import()` makes it a lazily-loaded route: Vite gives that route its own JavaScript chunk, which is not downloaded until the route is visited.

7. Import the router module into `main.js` and install it on the app.

   ```js
   import router from './router'

   app.use(createPinia())
   app.use(router)
   app.mount('#app')
   ```

   Install Pinia before the router, so that navigation guards and route components can reach the stores.

8. Open `App.vue` and replace the `<HomeContent />` component with `<RouterView />`.

   ```vue
   <script setup>
   import { RouterView } from 'vue-router'

   import TheHeader from './components/TheHeader.vue'
   import TheFooter from './components/TheFooter.vue'
   </script>

   <template>
     <div id="app">
       <TheHeader />
       <RouterView />
       <TheFooter />
     </div>
   </template>
   ```

   `app.use(router)` does register `<RouterView>` and `<RouterLink>` globally, so the import is optional. Importing them explicitly is worth the one line: the editor can then resolve them, and the component says what it depends on.

9. Remove the import for `HomeContent` from `App.vue`.

10. Run the development server and open the application in your browser. It should work the same as before.

11. Open the `TheHeader` component for editing.

12. Find the Sign In link, and replace it with a `RouterLink` component:

    ```vue
    <RouterLink class="nav-link" active-class="active" :to="{ name: 'login' }">
      Sign In
    </RouterLink>
    ```

    > **Note:** in Vue Router 4 and later, `active-class` is applied on partial matches and `exact-active-class` on exact ones, so use `exact-active-class` if you need exact matching.

13. View the application in your browser and click on the Sign In link. It won't work yet, because the `login` route doesn't exist.

14. Create a new route, in `router/index.js`, with the name `login` and the path `/login`.

    ```js
    {
      name: 'login',
      path: '/login',
      component: () => import('@/components/LoginPage.vue'),
    },
    ```

15. Make a new component named `LoginPage` and put a login form in the template. (The ESLint config requires multi-word component names, so `Login` is not allowed.)

    ```vue
    <script setup>
    // The form is wired up to the auth store in the next lab.
    function onSubmit() {}
    </script>

    <template>
      <div>
        <h1>Log In Here</h1>
        <form @submit.prevent="onSubmit">
          <fieldset class="form-group">
            <input
              class="form-control form-control-lg"
              type="text"
              placeholder="Email"
            />
          </fieldset>
          <fieldset class="form-group">
            <input
              class="form-control form-control-lg"
              type="password"
              placeholder="Password"
            />
          </fieldset>
          <button class="btn btn-lg btn-primary pull-xs-right">Sign in</button>
        </form>
      </div>
    </template>
    ```

16. Use `<RouterLink>` to link the logo to the home page.

    ```vue
    <RouterLink class="navbar-brand" :to="{ name: 'home' }">
      Conduit
    </RouterLink>
    ```

17. Link the Home navigation link to the home page the same way.

18. **Challenge:** make the Sign Up page and route.

19. **Challenge:** use a `<RouterView>` inside `HomeContent.vue` to render a different list (or differently-styled list) of articles when the user clicks a link. **Hint:** add a `children` property to the home route and make it an array of route objects.
