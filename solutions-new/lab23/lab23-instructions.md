# Lab 23: Testing with Vitest

If you run the unit tests in your project now, you'll see that the test on `HomeContent.vue` fails. `HomeContent.vue` now depends on the router and on a Pinia store, and neither exists inside a bare `mount()`. In this lab, you'll learn how to provide them.

1. Run `npm run test` and read the failure carefully. The message names the injection that could not be resolved.

2. Visit <https://test-utils.vuejs.org/guide/> and read about the `global.plugins` mounting option.

   > **Note:** Vue Test Utils 1 used `createLocalVue()` to install plugins without polluting the global Vue. Vue 3 apps are already isolated, so `createLocalVue` is gone. Plugins are passed per-mount through `global.plugins`.

3. Open `tests/components/HomeContent.spec.js` and create a router for the test.

   ```js
   import { createRouter, createWebHistory } from 'vue-router'

   const router = createRouter({
     history: createWebHistory(),
     routes: [{ name: 'home', path: '/', component: { template: '<div />' } }],
   })
   ```

4. Create a fresh Pinia instance before each test.

   ```js
   import { createPinia, setActivePinia } from 'pinia'

   let pinia

   beforeEach(() => {
     pinia = createPinia()
     setActivePinia(pinia)
   })
   ```

   Creating the Pinia instance per test keeps store state from leaking from one test into the next.

5. Pass both plugins when you mount the component.

   ```js
   const createWrapper = () =>
     shallowMount(HomeContent, { global: { plugins: [pinia, router] } })
   ```

   `shallowMount` stubs out child components, so `GlobalFeed` never mounts. `HomeContent` itself still requests `/tags` when it mounts, so add a `vi.mock()` for `@/common/api.service` that returns `{ data: { tags: [] } }` and keeps the test off the network.

6. Run `npm run test` again and confirm every test passes.

7. **Challenge:** write a test for the auth store itself. A Pinia store can be tested without mounting any component: call `useAuthStore()` after `setActivePinia()` and assert on its state.

8. **Challenge:** use `vi.mock()` to fake the `api.service` module so the store test never touches the network.
