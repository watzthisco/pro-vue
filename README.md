# Professional Vue.js

Labs, solutions and demos for the **Professional Vue.js** course, written by
Chris Minnick.

## Stack

Course version 2.0 targets the current Vue 3 toolchain:

| Tool                    | Version | Replaces                     |
| ----------------------- | ------- | ---------------------------- |
| Vue                     | 3.5     | Vue 2.6                      |
| Vite                    | 8       | Vue CLI 3 / webpack          |
| Pinia                   | 4       | Vuex 3                       |
| Vue Router              | 5       | Vue Router 3                 |
| Vitest + Vue Test Utils | 4 / 2   | Jest + Vue Test Utils 1      |
| ESLint (flat config)    | 10      | ESLint 5 (`.eslintrc.js`)    |
| axios                   | 1       | axios 0.18 + `vue-axios`     |

Components are written with the Composition API and `<script setup>`.

## Requirements

- Node.js 20.19+ or 22.12+ (`node --version`)
- npm 10+
- A code editor — Visual Studio Code with the **Vue - Official** extension is
  what the course uses

## Layout

| Directory      | Contents                                                  |
| -------------- | --------------------------------------------------------- |
| `labs/`        | Starter files students begin each lab from                 |
| `solutions/`   | Completed solution for each lab                            |
| `demos/`       | Standalone demos used during the lectures                  |
| `setup-test/`  | A minimal project for verifying a classroom setup          |
| `presentation/`| Slides, lab manual and course description, by version      |
| `quiz/`        | Daily review questions                                     |

## Running a lab or solution

Every Vue project in this repository is a self-contained Vite app:

```
cd solutions/lab24
npm install
npm run dev
```

Other scripts:

```
npm run build     # production build into dist/
npm run preview   # serve the production build
npm run test      # run the unit tests once with Vitest
npm run lint      # ESLint, with --fix
```

### API configuration

Labs 16 and later call the public Conduit (RealWorld) API. The default base URL
lives in `src/common/config.js`. To point a class at a different server, create
a `.env.local` file in the project root:

```
VITE_API_URL=https://your-conduit-host/api
```
