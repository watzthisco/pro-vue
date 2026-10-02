# Lab 22: AJAX

In this lab, you'll implement sign up functionality along with login and checking of authorization.

1. Copy `jwt.service.js` and `api.service.js` from `labs/lab22/common` into `src/common`, overwriting your existing `api.service.js`.

   The new `api.service.js` adds the `get`, `post`, `put` and `delete` helpers the auth store needs, plus a `setHeader()` method that attaches the stored token to every subsequent request.

2. Copy `stores/auth.js` from `labs/lab22/stores` into `src/stores`.

3. Open `src/stores/auth.js` and read through it. Note the shape:

   - `state` holds `errors`, `user`, and `isAuthenticated`, which is seeded from whatever token is already in `localStorage`.
   - `setAuth` and `purgeAuth` are ordinary actions. In the Vuex version these were the `SET_AUTH` and `PURGE_AUTH` mutations, referred to through string constants in `mutations.type.js`. Pinia needs neither the constants nor the file.
   - `login`, `register`, `checkAuth` and `updateUser` are `async` actions that call the API and then call `setAuth`. They store the server's validation errors on `state.errors` and re-throw, so the component can decide what to do.

4. Copy `Login.vue` and `Register.vue` from `labs/lab22/components` into `src/components`. The ESLint config requires multi-word component names, so save them as `LoginPage.vue` and `SignUpPage.vue`, overwriting your existing versions.

5. Open `LoginPage.vue` and note how the component talks to the store.

   ```js
   const router = useRouter()
   const authStore = useAuthStore()
   const { errors } = storeToRefs(authStore)

   async function onSubmit() {
     try {
       await authStore.login({ email: email.value, password: password.value })
       router.push({ name: 'home' })
     } catch {
       // Errors are surfaced through the store's `errors` state.
     }
   }
   ```

   > **Note:** inside `<script setup>` there is no `this`, so `this.$router` and `this.$store` are not available. `useRouter()` and the store's own `use` function are the Composition API equivalents. `useRoute()` gives you the current route object.

6. Make sure `router/index.js` has a `register` route pointing at `SignUpPage.vue`.

7. Test it out by registering and then by logging in.

8. Import the auth store and `storeToRefs` into `HomeContent.vue`.

   ```js
   import { storeToRefs } from 'pinia'

   import { useAuthStore } from '@/stores/auth'

   const { isAuthenticated } = storeToRefs(useAuthStore())
   ```

   The Vuex version used `...mapGetters(['isAuthenticated'])` inside a `computed` option. `storeToRefs` is the direct replacement, and it works on state as well as getters.

9. Use `isAuthenticated` in `HomeContent.vue` to conditionally show a logged-in user message in the sidebar.

    ```vue
    <p v-if="isAuthenticated">Welcome, authenticated user</p>
    ```

    > **Note:** the Vue 2 version of these components displayed errors with a filter: `{{ v | error }}`. Filters were removed in Vue 3. Use a method, a computed property, or an inline expression instead; `LoginPage.vue` joins the array of messages inline.

10. **Challenge:** display a logout button instead of the Login and Sign Up buttons when a user is logged in.

11. **Challenge:** call the auth store's `checkAuth()` action when the app starts, so a returning user with a valid token is logged straight back in.
