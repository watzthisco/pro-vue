# Lab 19 — Composables

Vue 3 replaces mixins with **composables**: plain functions that use the
Composition API and return the state and behaviour a component needs.

The filter logic that used to live in `src/mixins/filter.js` now lives in
`src/composables/useArticleFilter.js` and is called explicitly:

```js
const { searchDetails, filterIt } = useArticleFilter(articles);
```

Unlike a mixin, a composable:

- takes its inputs as arguments instead of reaching into `this`
- returns its outputs explicitly, so there are no silent name collisions
- can be called more than once in the same component

Mixins still work in Vue 3, but they are documented as legacy and should not be
used in new code.
