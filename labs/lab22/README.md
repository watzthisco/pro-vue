# Lab 22 handout files

Copy these into your `conduit` project:

| File                       | Destination                    |
| -------------------------- | ------------------------------ |
| `common/api.service.js`    | `src/common/api.service.js`    |
| `common/jwt.service.js`    | `src/common/jwt.service.js`    |
| `stores/auth.js`           | `src/stores/auth.js`           |
| `components/Login.vue`     | `src/components/Login.vue`     |
| `components/Register.vue`  | `src/components/Register.vue`  |

The auth store is a Pinia store. Pinia has no mutations, so what used to be a
mutation in Vuex is now just an action that assigns to `this`.
