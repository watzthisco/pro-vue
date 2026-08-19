"""Replacement slide text for Professional Vue.js v2.0 (2026).

Keys are 1-based slide numbers in the v1.5 deck. Each value is a dict with
optional 'title' and 'body'; body is a list of (indent level, text).
"""

REWRITE = {
    1: dict(title='Professional Vue.js Development'),

    9: dict(body=[
        (0, 'ES2015 (aka ES6) introduced many new features, including:'),
        (1, 'Arrow functions'),
        (1, 'Classes'),
        (1, 'Block-scoped binding constructs (let and const)'),
        (1, 'Iterators'),
        (1, 'Modules'),
        (1, 'Promises'),
        (0, 'Since 2015, a new version is released annually'),
        (1, 'ES2020: optional chaining (?.), nullish coalescing (??)'),
        (1, 'ES2021: String.replaceAll, logical assignment'),
        (1, 'ES2022: top-level await, class fields, Array.at'),
        (1, 'ES2024: Object.groupBy, Promise.withResolvers'),
    ]),

    12: dict(body=[
        (0, 'Created by Evan You after working for Google using AngularJS'),
        (1, '"I figured, what if I could just extract the part that I really '
            'liked about Angular and build something really lightweight."'),
        (0, 'Vue was originally released in February 2014.'),
        (0, 'Vue 3 shipped in September 2020 and became the default in 2022.'),
        (0, 'Vue 2 reached end of life on 31 December 2023.'),
    ]),

    13: dict(body=[
        (0, 'Incrementally adoptable'),
        (1, 'You can use it with just a script include'),
        (1, 'or, you can use it with modern tooling'),
        (0, 'Combines many of the best features of React and Angular'),
        (1, 'Has more built-in features than React'),
        (1, 'Less complex than Angular'),
        (0, 'Small! (~34kb gzipped for the runtime + reactivity)'),
        (1, 'Unused features are tree-shaken out of the bundle'),
        (0, 'Not created by a giant corporation'),
        (0, 'Governed by an independent team, funded by its users'),
    ]),

    15: dict(body=[
        (0, 'Vue and Angular have 2-way data binding'),
        (1, 'Detects changes to the data model and updates the view '
            'automatically.'),
        (1, 'Detects changes to the view and updates the data model '
            'automatically.'),
        (0, 'React has 1-way data binding'),
        (1, 'Developers write functions or use a state management system to '
            'update the model when events happen.'),
        (1, 'When the component re-renders, the view is updated from state.'),
        (0, 'Vue and Angular have built-in utility attributes (directives)'),
        (1, 'v-for, v-on, v-bind, v-model'),
        (0, 'React is mostly just pure JavaScript'),
        (0, 'All three now favour a function-based, composable component style'),
        (1, 'Vue: the Composition API; React: hooks; Angular: signals'),
    ]),

    16: dict(title='Demo: Vue.js Hello World', body=[
        (0, '<div id="app">'),
        (0, '  {{ message }}'),
        (0, '</div>'),
        (0, ''),
        (0, "import { createApp } from 'vue'"),
        (0, ''),
        (0, 'createApp({'),
        (0, '  data() {'),
        (0, "    return { message: 'Hello Vue!' }"),
        (0, '  }'),
        (0, "}).mount('#app')"),
        (0, ''),
        (0, '// Vue 2 wrote: new Vue({ el: "#app", data: { ... } })'),
    ]),

    19: dict(body=[
        (0, '1.0 - improved template syntax, v-for, hot reloading, scoped CSS'),
        (0, '2.0 - virtual DOM, JSX support, server-side rendering'),
        (0, '3.0 - Composition API, Teleport, Fragments, Proxy reactivity'),
        (0, '3.2 - <script setup>, v-memo, custom-element build'),
        (0, '3.3 - generic components, better TypeScript for defineProps'),
        (0, '3.4 - faster parser, stabilised defineModel'),
        (0, '3.5 - reactive props destructure, lazy hydration, lower memory'),
    ]),

    20: dict(title='What Vue 3 Changed', body=[
        (0, 'Reactivity rebuilt on Proxy'),
        (1, 'Added and deleted properties are now tracked; Vue.set is gone'),
        (0, 'The Composition API, and <script setup> on top of it'),
        (0, 'Fragments: a component may have more than one root element'),
        (0, 'Teleport: render part of a component elsewhere in the DOM'),
        (0, 'Multiple app instances, each isolated — there is no global Vue'),
        (0, 'First-class TypeScript support'),
        (0, 'Removed: filters, $on/$off/$once, functional component syntax'),
    ]),

    21: dict(title='Vue QuickStart', body=[
        (0, 'Objectives'),
        (1, 'Scaffold a project with create-vue'),
        (1, 'Understand what Vite gives you'),
        (1, 'Run, build and test a Vue app'),
    ]),

    24: dict(title='Vite', body=[
        (0, 'The build tool behind the current Vue tooling'),
        (0, 'Development: serves your source as native ES modules'),
        (1, 'No bundling step, so startup and reloads stay fast as the app grows'),
        (1, 'Hot module replacement that keeps component state'),
        (0, 'Production: bundles and minifies with Rollup'),
        (0, 'Framework-agnostic — Vue support comes from @vitejs/plugin-vue'),
        (0, 'Vue CLI, which used webpack, reached end of life at the end of 2023'),
    ]),

    25: dict(title='Using create-vue', body=[
        (0, 'Scaffold a project — nothing to install globally'),
        (1, 'npm create vue@latest'),
        (0, 'Then, in the new directory:'),
        (1, 'npm install'),
        (1, 'npm run dev      # start the dev server on :5173'),
        (1, 'npm run build    # production build into dist/'),
        (1, 'npm run preview  # serve the production build'),
        (0, 'The prompts let you add Router, Pinia, Vitest, ESLint up front'),
    ]),

    26: dict(title='Lab 02: Get Started with Vite'),

    28: dict(title='Our Real-world Project: Conduit'),

    29: dict(body=[
        (0, 'Modern JS frameworks use modules to create reusable components.'),
        (0, 'Components are composed into user interfaces.'),
        (0, "Vue's components are called \"Single File Components\""),
        (1, 'They encapsulate Template, Script, and Style'),
        (0, 'We write them with <script setup>, the Composition API syntax'),
        (1, 'Every top-level binding is available to the template'),
        (1, 'The import of a child component is its registration'),
    ]),

    31: dict(title='Lab 05: Testing Vue', body=[
        (0, 'Write your first Vue tests with Vitest and Vue Test Utils.'),
    ]),

    48: dict(title='Other package managers', body=[
        (0, 'npm ships with Node.js and is the default'),
        (0, 'yarn — created by Facebook; Plug\'n\'Play install mode'),
        (0, 'pnpm — hard-links a global store, so disk use stays flat'),
        (1, 'Strict by default: a package can only import what it declares'),
        (0, 'bun — a runtime with a very fast built-in installer'),
        (0, 'All four read package.json; they differ in the lockfile'),
    ]),

    52: dict(title='npm install', body=[
        (0, 'Is used to download and install a package'),
        (1, '(no flag): saves to dependencies — this is the default'),
        (1, '--save-dev (-D): saves to devDependencies'),
        (1, '--save-optional: saves to optionalDependencies'),
        (1, '--save-exact (-E): pins the exact version, no range operator'),
        (1, '--global (-g): installs to a shared location, not the project'),
        (0, 'npm ci installs strictly from the lockfile — use it in CI'),
    ]),

    55: dict(title='Demo / Code-along: Set up your own tooling', body=[
        (0, 'How to create a Vue.js app with single-file components, starting '
            'from an empty directory.'),
        (0, 'github.com/watzthisco/pro-vue/demos/Vue-Starter'),
        (0, 'Three dependencies: vue, vite, @vitejs/plugin-vue'),
    ]),

    58: dict(title='Configuring ESLint', body=[
        (0, 'Two ways'),
        (1, 'Configuration comments'),
        (2, 'embed configuration info in JS files with comments'),
        (2, '/* eslint eqeqeq: "off", curly: "error" */'),
        (1, 'Configuration files'),
        (2, 'eslint.config.js — the "flat config" format'),
        (0, 'Flat config became the default in ESLint 9'),
        (1, 'It exports an array; each entry applies to the files it matches'),
        (1, '.eslintrc.* and .eslintignore were removed in ESLint 10'),
    ]),

    59: dict(body=[
        (0, 'languageOptions'),
        (1, 'ecmaVersion, sourceType, and the parser to use'),
        (1, 'globals — the predefined variables the code can rely on'),
        (0, 'files / ignores'),
        (1, 'Which paths this configuration object applies to'),
        (0, 'plugins'),
        (1, 'Imported objects now, not strings resolved by name'),
        (0, 'rules'),
        (1, 'Enable rules at different levels'),
    ]),

    61: dict(body=[
        (0, 'Install ESLint into the project'),
        (0, 'Write an eslint.config.js flat config'),
        (0, 'Create an npm script called "lint"'),
        (0, 'Make the lint task a dependency of the default build task'),
    ]),

    62: dict(title='Transpilers', body=[
        (0, 'Not all browsers support the same JavaScript and CSS features.'),
        (0, 'https://caniuse.com'),
        (0, 'Transpilers convert modern code to a form older browsers accept.'),
        (0, 'Vite does this for you at build time, guided by browserslist.'),
        (1, 'esbuild handles the syntax; the target defaults to browsers with '
            'native ES module support.'),
    ]),

    64: dict(title='Babel and esbuild', body=[
        (0, 'Babel is a transpiler.'),
        (1, 'Plugin-based, and the reference implementation for new syntax'),
        (0, 'Vite uses esbuild instead for its dev-time transform'),
        (1, 'Written in Go, and roughly two orders of magnitude faster'),
        (0, 'You rarely configure either one directly in a Vite project'),
    ]),

    66: dict(title='Bundlers', body=[
        (0, 'A bundler resolves your import graph and writes deployable files.'),
        (0, 'webpack — the incumbent; configured with loaders and plugins'),
        (0, 'Rollup — what Vite uses for production builds'),
        (0, 'esbuild — what Vite uses to pre-bundle dependencies'),
        (0, 'In development Vite does not bundle your source at all.'),
    ]),

    67: dict(title='How Vite Works', body=[
        (0, 'In development'),
        (1, 'Serves your source over HTTP as native ES modules'),
        (1, 'Transforms each file only when the browser asks for it'),
        (1, 'Pre-bundles dependencies once with esbuild, then caches them'),
        (0, 'In production'),
        (1, 'Bundles with Rollup: tree-shaking, code-splitting, minification'),
        (1, 'Each lazily-imported route becomes its own chunk'),
        (0, 'Plugins extend both pipelines — @vitejs/plugin-vue compiles SFCs'),
    ]),

    82: dict(title='Installing and Using the Vue DevTools'),

    86: dict(title='Creating and Mounting an App', body=[
        (0, "import { createApp } from 'vue'"),
        (0, "import App from './App.vue'"),
        (0, ''),
        (0, 'const app = createApp(App)   // an isolated application instance'),
        (0, ''),
        (0, 'app.use(createPinia())       // plugins are installed per app'),
        (0, 'app.use(router)'),
        (0, "app.mount('#app')           // where to render"),
        (0, ''),
        (0, '// There is no global Vue object, so two apps on the same page'),
        (0, '// never share plugins, components, or configuration.'),
    ]),

    87: dict(title='App-level Configuration', body=[
        (0, 'app.component(name, Component) — register globally'),
        (0, 'app.directive(name, definition) — register a custom directive'),
        (0, 'app.use(plugin) — install a plugin'),
        (0, 'app.provide(key, value) — provide a value to every descendant'),
        (0, 'app.config.errorHandler — catch errors from any component'),
        (0, 'app.mount(selector) / app.unmount()'),
        (0, 'Vue 2 set all of these on the global Vue; Vue 3 scopes them to '
            'the app instance.'),
    ]),

    88: dict(title='Vue Template Syntax', body=[
        (0, '<script setup>'),
        (0, "import { computed, ref } from 'vue'"),
        (0, ''),
        (0, "const message = ref('Hello')          // state"),
        (0, 'const shouted = computed(() => message.value.toUpperCase())'),
        (0, ''),
        (0, 'function reset() { message.value = \'\' }  // behaviour'),
        (0, '</script>'),
    ]),

    96: dict(title='Custom Directives', body=[
        (0, 'Components are the main way to reuse code.'),
        (0, 'Still, there may be times when you need low-level DOM access on '
            'plain elements.'),
        (0, ''),
        (0, 'const vFocus = {'),
        (0, '  mounted: (el) => el.focus()'),
        (0, '}'),
        (0, ''),
        (0, '<input v-focus>'),
        (0, ''),
        (0, '// In <script setup>, a const named vName is usable as v-name.'),
        (0, '// The hook names now match the component lifecycle: what Vue 2'),
        (0, '// called "inserted" is "mounted".'),
    ]),

    97: dict(body=[
        (0, 'Use the v-for directive to render a list of items from an array '
            'or object'),
        (0, '<ul>'),
        (0, '  <li v-for="song in songs" :key="song.id">'),
        (0, '    {{ song.title }}'),
        (0, '  </li>'),
        (0, '</ul>'),
        (0, ''),
        (0, "const songs = ref([{ id: 1, title: 'Hotel California' }])"),
    ]),

    98: dict(body=[
        (0, 'Always provide a key with v-for.'),
        (0, ''),
        (0, '<li v-for="song in songs" :key="song.id">'),
        (0, '  {{ song.title }}'),
        (0, '</li>'),
        (0, ''),
        (0, "Providing a key helps Vue track each node's identity."),
        (0, 'The key goes on the element that carries v-for — including on a '
            '<template v-for>, which Vue 2 did not allow.'),
        (0, 'Use a stable id, not the array index.'),
    ]),
}

REWRITE.update({
    104: dict(title='Lab 11: Static Vue View'),

    108: dict(body=[
        (0, ':class can be used to dynamically toggle classes'),
        (0, '<div :class="{ active: isActive }"></div>'),
        (0, 'pass an array to :class to apply a list of classes'),
        (0, '<div :class="[baseClass, { active: isActive }]"></div>'),
        (0, 'Vue merges these with any static class attribute on the element.'),
    ]),

    109: dict(body=[
        (0, 'You can bind a computed property or a ref to the class attribute '
            'to change styles based on conditions.'),
        (0, ''),
        (0, '<div :class="[{ active: isActive }, errorClass]"></div>'),
        (0, ''),
        (0, 'const errorClass = computed(() => (hasError.value ? \'text-danger\' : \'\'))'),
    ]),

    110: dict(body=[
        (0, 'Inline object syntax for :style'),
        (0, '<div :style="{ color: activeColor, fontSize: fontSize + \'px\' }">'),
        (0, '</div>'),
        (0, ''),
        (0, 'Bind to a style object to keep the template cleaner'),
        (0, ''),
        (0, '<div :style="styleObject"></div>'),
        (0, ''),
        (0, 'const styleObject = reactive({'),
        (0, "  color: 'red',"),
        (0, "  fontSize: '13px'"),
        (0, '})'),
    ]),

    113: dict(title='Computed Properties', body=[
        (0, "import { computed, ref } from 'vue'"),
        (0, ''),
        (0, "const firstName = ref('Ada')"),
        (0, "const lastName = ref('Lovelace')"),
        (0, ''),
        (0, 'const fullName = computed('),
        (0, '  () => `${firstName.value} ${lastName.value}`'),
        (0, ')'),
    ]),

    114: dict(body=[
        (0, 'Useful for operations too complex to sit in a template.'),
        (0, 'Created by calling computed() with a getter function.'),
        (0, ''),
        (0, "const message = ref('Hi There')"),
        (0, ''),
        (0, 'const reversedMessage = computed(() =>'),
        (0, "  message.value.split('').reverse().join('')"),
        (0, ')'),
        (0, ''),
        (0, '// computed() returns a ref, so read it as reversedMessage.value'),
        (0, '// in script and as reversedMessage in the template.'),
    ]),

    115: dict(body=[
        (0, 'Unlike a plain function call, a computed property is cached and '
            'will not re-run unless a reactive value it read has changed.'),
        (0, 'Can often be used instead of a watcher.'),
        (0, 'A getter should have no side effects — do not mutate state or '
            'make requests inside one.'),
    ]),

    117: dict(body=[
        (0, 'Computed properties are getter-only by default.'),
        (0, 'Pass an object with get and set when you need to write to one.'),
        (0, ''),
        (0, 'const fullName = computed({'),
        (0, '  get: () => `${firstName.value} ${lastName.value}`,'),
        (0, '  set: (newValue) => {'),
        (0, "    const names = newValue.split(' ')"),
        (0, '    firstName.value = names[0]'),
        (0, '    lastName.value = names.at(-1)'),
        (0, '  }'),
        (0, '})'),
    ]),

    119: dict(title='Reactive State', body=[
        (0, "import { reactive, ref } from 'vue'"),
        (0, ''),
        (0, 'const count = ref(0)              // any value; use .value'),
        (0, "const user = reactive({ name: '' })  // objects only; no .value"),
        (0, ''),
        (0, '// A ref is the default choice. reactive() cannot hold a'),
        (0, '// primitive, and loses reactivity if you destructure it.'),
    ]),

    120: dict(title='ref and reactive', body=[
        (0, 'State lives in refs, declared at the top of <script setup>.'),
        (0, 'When a ref changes, every component that read it re-renders.'),
        (0, 'Vue 3 tracks state with a Proxy, so properties added or deleted '
            'after creation are reactive too.'),
        (0, 'Vue.set and vm.$set existed only to work around that limit in '
            'Vue 2, and were removed.'),
    ]),

    121: dict(body=[
        (0, 'Use the v-bind directive (shorthand :) to bind an attribute to a '
            'reactive value — one-way binding.'),
        (0, 'Vue keeps the attribute up to date with the value.'),
        (0, 'Use the v-model directive to create two-way binding between an '
            'input and a ref.'),
    ]),

    123: dict(body=[
        (0, 'Use v-bind to bind the value of a radio, checkbox, or select '
            'option to a dynamic value.'),
        (0, '<input type="checkbox" v-model="toggle" true-value="yes" '
            'false-value="no">'),
        (0, '<input type="radio" v-model="pick" :value="a">'),
    ]),

    126: dict(title='Working with Arrays', body=[
        (0, 'All array mutations are reactive, because Vue 3 observes the '
            'array through a Proxy:'),
        (1, 'push, pop, shift, unshift, splice, sort, reverse'),
        (1, 'items[0] = value — assignment by index'),
        (1, 'items.length = 0'),
        (0, 'Vue 2 could not detect the last two, and needed Vue.set and '
            'splice as workarounds.'),
        (0, 'Replacing the array wholesale is still often clearer:'),
        (1, 'items.value = items.value.filter(...)'),
    ]),

    127: dict(title='Reactivity Caveats', body=[
        (0, 'Proxy-based reactivity is deep and covers add and delete, but a '
            'few things still break tracking:'),
        (0, 'Destructuring a reactive() object copies the values out'),
        (1, 'Use toRefs() — or a ref — instead'),
        (0, 'Replacing a reactive() object wholesale drops the old proxy'),
        (0, 'Reassigning a ref without .value inside <script setup>'),
        (0, 'Map, Set, Date and class instances are supported, but a plain '
            'object is usually the simpler choice.'),
    ]),

    128: dict(title='Destructuring and Reactivity', body=[
        (0, 'const state = reactive({ count: 0 })'),
        (0, 'const { count } = state       // count is now a plain 0'),
        (0, ''),
        (0, 'const { count } = toRefs(state)  // count is a ref — still live'),
        (0, ''),
        (0, '// The same rule applies to Pinia stores, which is why you'),
        (0, '// destructure them through storeToRefs().'),
    ]),

    131: dict(body=[
        (0, 'The v-on directive (shorthand @) creates an event listener.'),
        (0, '<button @click="counter += 1">Add 1</button>'),
        (0, '<p>The button has been clicked {{ counter }} times.</p>'),
        (0, ''),
        (0, "import { ref } from 'vue'"),
        (0, ''),
        (0, 'const counter = ref(0)'),
    ]),

    133: dict(title='Event Handling with Methods', body=[
        (0, 'Declare a function in <script setup> and call it from v-on.'),
        (0, ''),
        (0, "const name = ref('Vue.js')"),
        (0, ''),
        (0, 'function greet(event) {'),
        (0, '  alert(`Hello ${name.value}!`)'),
        (0, '  if (event) alert(event.target.tagName)'),
        (0, '}'),
        (0, ''),
        (0, '<button @click="greet">Greet</button>'),
    ]),

    136: dict(body=[
        (0, 'Child components declare and emit events'),
        (0, "const emit = defineEmits(['enlarge-text'])"),
        (0, '<button @click="emit(\'enlarge-text\')">Enlarge text</button>'),
        (0, ''),
        (0, 'Parent components listen for them'),
        (0, '<BlogPost @enlarge-text="postFontSize += 0.1" />'),
        (0, ''),
        (0, '// An undeclared listener falls through to the root element as a'),
        (0, '// native attribute, so always declare your events.'),
    ]),

    137: dict(body=[
        (0, 'emit can take further arguments'),
        (0, "const emit = defineEmits(['enlarge-text'])"),
        (0, '<button @click="emit(\'enlarge-text\', 0.1)">Enlarge text</button>'),
        (0, ''),
        (0, 'The parent receives them as handler arguments'),
        (0, '<BlogPost @enlarge-text="postFontSize += $event" />'),
        (0, '<BlogPost @enlarge-text="(n) => postFontSize += n" />'),
        (0, ''),
        (0, '// Vue 2 also offered $on / $off / $once for an "event bus".'),
        (0, '// Those were removed in Vue 3 — use a store or provide/inject.'),
    ]),

    139: dict(title='Watchers', body=[
        (0, 'A general way to react to state changes.'),
        (0, 'Most useful for asynchronous or expensive work in response to '
            'changing data.'),
        (0, ''),
        (0, "const question = ref('')"),
        (0, "const answer = ref('Ask me a question!')"),
        (0, ''),
        (0, 'watch(question, async (newQuestion, oldQuestion) => {'),
        (0, "  answer.value = 'Thinking...'"),
        (0, '  answer.value = await getAnswer(newQuestion)'),
        (0, '})'),
    ]),

    140: dict(title='watch and watchEffect', body=[
        (0, 'watch(source, callback)'),
        (1, 'Explicit about what it tracks; gives you the old value'),
        (1, 'Lazy — the callback does not run until the source changes'),
        (0, 'watchEffect(callback)'),
        (1, 'Tracks whatever the callback reads, automatically'),
        (1, 'Runs once immediately'),
        (0, 'Both return a stop function, and both stop automatically when '
            'the component unmounts.'),
        (0, 'Reach for computed() first — a watcher is for side effects.'),
    ]),

    141: dict(title='Component Lifecycle', body=[
        (0, 'Functions imported from vue and called inside <script setup>'),
        (1, 'onBeforeMount / onMounted'),
        (1, 'onBeforeUpdate / onUpdated'),
        (1, 'onBeforeUnmount / onUnmounted'),
        (1, 'onErrorCaptured, onActivated, onDeactivated'),
        (0, 'There is no onCreated — the body of <script setup> is that hook.'),
        (0, 'Vue 2 named the last pair beforeDestroy and destroyed.'),
    ]),

    142: dict(title='Setup (replacing beforeCreate / created)', body=[
        (0, 'The body of <script setup> runs before the component is mounted.'),
        (0, 'State and props exist; there is no DOM yet.'),
        (0, 'This is where you declare refs, computed values and functions, '
            'and start any request whose result the first render does not '
            'need.'),
    ]),

    143: dict(title='onBeforeMount', body=[
        (0, 'Runs after the template has been compiled but before the first '
            'render.'),
        (0, ''),
        (0, 'onBeforeMount(() => {'),
        (0, "  console.log('about to render')"),
        (0, '})'),
        (0, ''),
        (0, 'Rarely needed.'),
    ]),

    144: dict(title='onMounted', body=[
        (0, 'Full access to the rendered DOM through template refs.'),
        (0, 'Use for measuring elements and integrating non-Vue libraries.'),
        (0, ''),
        (0, 'onMounted(async () => {'),
        (0, '  articles.value = await fetchArticles()'),
        (0, '})'),
        (0, ''),
        (0, 'A child is mounted before its parent.'),
    ]),

    145: dict(title='onBeforeUpdate', body=[
        (0, 'Runs after state changes, before the DOM is patched.'),
        (0, 'Use it to read the DOM as it was before the update — for example '
            'to record a scroll position.'),
    ]),

    146: dict(title='onUpdated', body=[
        (0, 'Runs after state changes and the DOM has re-rendered.'),
        (0, 'Do not change state here without a guard — you will loop.'),
        (0, 'To react to one specific value, prefer watch().'),
    ]),

    147: dict(title='onBeforeUnmount', body=[
        (0, 'Fires right before teardown, while the component is still fully '
            'functional.'),
        (0, 'Use it to clean up timers, subscriptions and listeners you '
            'created yourself.'),
    ]),

    148: dict(title='onUnmounted', body=[
        (0, 'Everything attached to the component has been torn down and '
            'removed from the DOM.'),
        (0, 'Watchers and lifecycle hooks are stopped for you; anything you '
            'set up by hand is not.'),
    ]),

    149: dict(title='Lifecycle Hooks in Practice', body=[
        (0, '<script setup>'),
        (0, "import { onMounted, onUnmounted, ref } from 'vue'"),
        (0, ''),
        (0, 'const seconds = ref(0)'),
        (0, 'let timer'),
        (0, ''),
        (0, 'onMounted(() => {'),
        (0, '  timer = setInterval(() => seconds.value++, 1000)'),
        (0, '})'),
        (0, ''),
        (0, 'onUnmounted(() => clearInterval(timer))'),
        (0, '</script>'),
    ]),

    150: dict(title='Using Lifecycle Hooks', body=[
        (0, 'Hooks must be called synchronously in the body of <script setup>'),
        (1, 'Not inside a callback, a promise handler, or a condition'),
        (0, 'That is how Vue knows which component instance to attach them to'),
        (0, 'They can be called from a composable, because a composable is '
            'itself called synchronously from setup'),
    ]),
})

REWRITE.update({
    154: dict(body=[
        (0, '2-way binding makes development easier'),
        (0, '2-way binding makes testing more difficult'),
        (0, 'v-model is sort of magic (which could be a pro or con)'),
        (0, ''),
        (0, '<input v-model="searchText">'),
        (0, ''),
        (0, 'does the same thing as:'),
        (0, ''),
        (0, '<input'),
        (0, '  :value="searchText"'),
        (0, '  @input="searchText = $event.target.value" >'),
    ]),

    161: dict(title='What are Vue Components?', body=[
        (0, 'A reusable piece of UI with its own state, template and styles.'),
        (0, 'Written as a single-file component: .vue with <script setup>, '
            '<template> and <style>.'),
        (0, 'State is declared with ref() and reactive(), so each instance '
            'automatically gets its own copy — this is what the data() '
            'function guaranteed in the Options API.'),
        (0, 'A component may have more than one root element (a Fragment).'),
    ]),

    162: dict(title='Creating a Component', body=[
        (0, '<script setup>'),
        (0, 'defineProps({'),
        (0, '  todo: { type: Object, required: true }'),
        (0, '})'),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <li>{{ todo.text }}</li>'),
        (0, '</template>'),
        (0, ''),
        (0, '// The file name is the component name: TodoItem.vue is used as'),
        (0, '// <TodoItem />. Vue 2 wrote Vue.component("todo-item", { ... }).'),
    ]),

    164: dict(body=[
        (0, 'Two options'),
        (1, 'PascalCase — the recommended default'),
        (2, 'Matches the file name, and the editor can resolve it'),
        (2, 'Distinguishes your components from native HTML elements'),
        (1, 'kebab-case'),
        (2, 'Required when writing templates directly in the DOM, because '
            'HTML tag names are case-insensitive'),
        (0, 'A component imported in <script setup> can be used under the '
            'name you imported it as.'),
    ]),

    165: dict(title='Local Components', body=[
        (0, 'The usual case: import the component where you use it.'),
        (0, ''),
        (0, '<script setup>'),
        (0, "import PopupWindow from './components/PopupWindow.vue'"),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <PopupWindow />'),
        (0, '</template>'),
        (0, ''),
        (0, '// The import is the registration. There is no components option.'),
    ]),

    166: dict(title='Global Components', body=[
        (0, "import { createApp } from 'vue'"),
        (0, "import PopupWindow from './components/PopupWindow.vue'"),
        (0, "import App from './App.vue'"),
        (0, ''),
        (0, 'const app = createApp(App)'),
        (0, ''),
        (0, "app.component('PopupWindow', PopupWindow)"),
        (0, ''),
        (0, "app.mount('#app')"),
        (0, ''),
        (0, '// Registered on the app, not on a global Vue, so a second app'),
        (0, '// on the page does not see it.'),
    ]),

    167: dict(title='Global vs. Local', body=[
        (0, 'Prefer local registration.'),
        (1, 'A reader can see where every component comes from'),
        (1, 'Unused components can be tree-shaken out of the bundle'),
        (1, 'The editor can jump to the definition'),
        (0, 'Register globally only for components used on nearly every '
            'screen — an icon or a button primitive.'),
    ]),

    168: dict(title='Props', body=[
        (0, 'Declare props with the defineProps compiler macro.'),
        (0, ''),
        (0, 'const props = defineProps({'),
        (0, '  todo: { type: Object, required: true },'),
        (0, "  size: { type: String, default: 'medium' }"),
        (0, '})'),
        (0, ''),
        (0, '// In the template write todo directly;'),
        (0, '// in script go through props.todo.'),
        (0, '// Props are read-only — emit an event to ask for a change.'),
    ]),

    170: dict(title='Using Props', body=[
        (0, '<!-- parent -->'),
        (0, '<TodoItem :todo="item" size="large" />'),
        (0, ''),
        (0, '<!-- TodoItem.vue -->'),
        (0, '<script setup>'),
        (0, "defineProps(['todo', 'size'])"),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <li>{{ todo.text }}</li>'),
        (0, '</template>'),
    ]),

    171: dict(title='Fragments: Multiple Root Elements', body=[
        (0, 'Vue 2 required a single root element. Vue 3 does not.'),
        (0, ''),
        (0, '<template>'),
        (0, '  <h1>{{ title }}</h1>'),
        (0, '  <div v-html="content"></div>'),
        (0, '</template>'),
        (0, ''),
        (0, 'One caveat: with more than one root, Vue cannot decide where to '
            'put inherited attributes, so bind $attrs explicitly if the '
            'parent passes class or style.'),
    ]),

    172: dict(title='Using v-model on Components', body=[
        (0, 'v-model works on components as it does on inputs'),
        (0, ''),
        (0, '<CustomInput v-model="searchText" />'),
        (0, ''),
        (0, 'does the same thing as'),
        (0, ''),
        (0, '<CustomInput'),
        (0, '  :model-value="searchText"'),
        (0, '  @update:model-value="searchText = $event" />'),
        (0, ''),
        (0, '// Vue 2 used the value prop and the input event. Vue 3 renamed'),
        (0, '// them to modelValue and update:modelValue, which frees up'),
        (0, '// value for ordinary use and allows several v-models per'),
        (0, '// component: v-model:title, v-model:body.'),
    ]),

    173: dict(title='defineModel', body=[
        (0, 'Since Vue 3.4 the whole prop-and-event pair has a shorthand.'),
        (0, ''),
        (0, '<script setup>'),
        (0, 'const model = defineModel()'),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <input v-model="model">'),
        (0, '</template>'),
        (0, ''),
        (0, '// model is a writable ref. Writing to it emits the update event'),
        (0, '// for you.'),
    ]),

    181: dict(title='Loading Components Asynchronously', body=[
        (0, 'Wrap a dynamic import with defineAsyncComponent.'),
        (0, ''),
        (0, "import { defineAsyncComponent } from 'vue'"),
        (0, ''),
        (0, 'const AsyncModal = defineAsyncComponent(() =>'),
        (0, "  import('./components/Modal.vue')"),
        (0, ')'),
        (0, ''),
        (0, 'Vite gives the component its own chunk, downloaded on first use.'),
        (0, 'Routes get this for free from a lazy route component.'),
        (0, 'Pair it with <Suspense> to show a fallback while it loads.'),
    ]),

    182: dict(title='Composables'),

    183: dict(title='Composable Basics', body=[
        (0, 'A composable is a function that uses the Composition API to '
            'encapsulate and reuse stateful logic.'),
        (0, 'By convention it is named use* and lives in src/composables.'),
        (0, 'It is called synchronously from <script setup>, so it can use '
            'lifecycle hooks and watchers on the caller\'s behalf.'),
    ]),

    184: dict(title='Why Composables Replace Mixins', body=[
        (0, 'A mixin merged its options into the component silently:'),
        (1, 'You could not tell where an inherited property came from'),
        (1, 'Two mixins declaring the same name collided, and the winner was '
            'decided by a merge strategy'),
        (1, 'A mixin could not take arguments'),
        (0, 'A composable takes its inputs as parameters and returns its '
            'outputs, so both ends are visible at the call site.'),
        (0, 'Mixins still work in Vue 3, but are documented as legacy.'),
    ]),

    185: dict(title='Writing a Composable', body=[
        (0, "import { computed, ref } from 'vue'"),
        (0, ''),
        (0, 'export function useArticleFilter(articles) {'),
        (0, "  const searchDetails = ref('')"),
        (0, ''),
        (0, '  const filterIt = computed(() =>'),
        (0, '    articles.value.filter((a) =>'),
        (0, '      a.title.includes(searchDetails.value)'),
        (0, '    )'),
        (0, '  )'),
        (0, ''),
        (0, '  return { searchDetails, filterIt }'),
        (0, '}'),
    ]),

    186: dict(title='Using a Composable', body=[
        (0, '<script setup>'),
        (0, "import { ref } from 'vue'"),
        (0, "import { useArticleFilter } from '@/composables/useArticleFilter'"),
        (0, ''),
        (0, 'const articles = ref([])'),
        (0, ''),
        (0, 'const { searchDetails, filterIt } = useArticleFilter(articles)'),
        (0, '</script>'),
        (0, ''),
        (0, '// Called twice, you get two independent filters — something a'),
        (0, '// mixin could never do.'),
    ]),

    187: dict(title='Composable Conventions', body=[
        (0, 'Name it use* so readers know it may register hooks'),
        (0, 'Call it synchronously from setup, never in a callback'),
        (0, 'Accept refs or getters as arguments so callers can pass live '
            'state; toValue() normalises them'),
        (0, 'Return plain refs, so the caller can destructure freely'),
        (0, 'Clean up after yourself in onUnmounted'),
    ]),

    188: dict(title='Community Composables', body=[
        (0, 'VueUse — a large collection of ready-made composables'),
        (1, 'useLocalStorage, useFetch, useMediaQuery, useDebounce, ...'),
        (0, 'Worth checking before writing your own'),
        (0, 'vueuse.org'),
    ]),

    190: dict(title='Lab 19: Composables', body=[
        (0, 'Extract the filterIt computed property into a composable and use '
            'it from ArticleList.vue.'),
    ]),
})

REWRITE.update({
    # ---------------------------------------------------------- Pinia (191-217)
    191: dict(title='Using Pinia'),
    192: dict(title='Why a Store?'),

    193: dict(title='The Problem', body=[
        (0, 'Props flow down; events flow up.'),
        (0, 'That works until two distant components need the same state.'),
        (1, 'Passing it through every intermediate component ("prop drilling")'),
        (1, 'Two copies that drift out of sync'),
        (0, 'A store gives that state one owner, outside the component tree.'),
    ]),

    194: dict(title='Pinia', body=[
        (0, "Vue's official state management library."),
        (0, 'A store is a composable: you call useSomeStore() to get it.'),
        (0, 'state, getters and actions — no mutations, no dispatch, no commit.'),
        (0, 'Type-safe, and each store is its own module by construction.'),
        (0, 'Replaced Vuex, which is now in maintenance mode.'),
    ]),

    195: dict(title='Pinia vs. Vuex', body=[
        (0, 'Vuex                          Pinia'),
        (0, 'state                         state'),
        (0, 'getters                       getters'),
        (0, 'mutations                     — (actions assign directly)'),
        (0, "actions + dispatch('name')    actions, called as functions"),
        (0, "commit('NAME', payload)       this.value = payload"),
        (0, 'modules                       one file per store'),
        (0, 'mapState / mapGetters         storeToRefs'),
    ]),

    196: dict(title='Installing Pinia', body=[
        (0, 'npm install pinia'),
        (0, ''),
        (0, "import { createPinia } from 'pinia'"),
        (0, ''),
        (0, 'const app = createApp(App)'),
        (0, 'app.use(createPinia())'),
        (0, "app.mount('#app')"),
        (0, ''),
        (0, '// Install Pinia before the router, so navigation guards can'),
        (0, '// reach the stores.'),
    ]),

    197: dict(title='Defining a Store', body=[
        (0, "import { defineStore } from 'pinia'"),
        (0, ''),
        (0, "export const useCounterStore = defineStore('counter', {"),
        (0, '  state: () => ({ count: 0 }),'),
        (0, ''),
        (0, '  getters: {'),
        (0, '    double: (state) => state.count * 2'),
        (0, '  },'),
        (0, ''),
        (0, '  actions: {'),
        (0, '    increment() { this.count++ }'),
        (0, '  }'),
        (0, '})'),
        (0, ''),
        (0, "// 'counter' is the store id, used by the DevTools."),
    ]),

    198: dict(title='Setup Stores', body=[
        (0, 'A store can also be written like <script setup>.'),
        (0, ''),
        (0, "export const useCounterStore = defineStore('counter', () => {"),
        (0, '  const count = ref(0)                       // state'),
        (0, '  const double = computed(() => count.value * 2)  // getter'),
        (0, ''),
        (0, '  function increment() { count.value++ }     // action'),
        (0, ''),
        (0, '  return { count, double, increment }'),
        (0, '})'),
        (0, ''),
        (0, '// Same store, different syntax. Use whichever reads better;'),
        (0, '// setup stores compose more easily, option stores map more'),
        (0, '// directly onto a Vuex module you are porting.'),
    ]),

    199: dict(title='State', body=[
        (0, 'state is a function that returns a fresh object.'),
        (0, 'Read and write it directly on the store:'),
        (0, ''),
        (0, 'const counter = useCounterStore()'),
        (0, ''),
        (0, 'counter.count++'),
        (0, 'counter.$patch({ count: 10 })   // several changes at once'),
        (0, 'counter.$reset()                // back to the initial state'),
    ]),

    200: dict(title='Getters', body=[
        (0, 'Computed properties for a store.'),
        (0, 'Receive state as their first argument.'),
        (0, 'Cached, like any computed property.'),
        (0, ''),
        (0, 'getters: {'),
        (0, '  doneTodos: (state) => state.todos.filter((t) => t.done),'),
        (0, '  doneCount() { return this.doneTodos.length }'),
        (0, '}'),
        (0, ''),
        (0, '// Use `this` (and a normal function) to reach other getters.'),
    ]),

    201: dict(title='Using a Store in a Component', body=[
        (0, '<script setup>'),
        (0, "import { useCounterStore } from '@/stores/counter'"),
        (0, ''),
        (0, 'const counter = useCounterStore()'),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <p>{{ counter.count }} / {{ counter.double }}</p>'),
        (0, '  <button @click="counter.increment()">+1</button>'),
        (0, '</template>'),
    ]),

    202: dict(title='storeToRefs', body=[
        (0, 'A store is reactive, so destructuring it copies values out and '
            'breaks reactivity.'),
        (0, ''),
        (0, 'const { count, double } = counter        // WRONG — not reactive'),
        (0, ''),
        (0, "import { storeToRefs } from 'pinia'"),
        (0, ''),
        (0, 'const { count, double } = storeToRefs(counter)   // refs'),
        (0, 'const { increment } = counter                    // actions are'),
        (0, '                                                 // plain functions'),
        (0, ''),
        (0, '// storeToRefs is the replacement for mapState and mapGetters.'),
    ]),

    203: dict(title='Actions', body=[
        (0, 'An action is just a method on the store.'),
        (0, 'It may be async, and it assigns to state through this.'),
        (0, ''),
        (0, 'actions: {'),
        (0, '  async fetchArticles(params) {'),
        (0, '    this.isLoading = true'),
        (0, '    try {'),
        (0, '      const { data } = await ArticlesService.query(params.type)'),
        (0, '      this.articles = data.articles'),
        (0, '    } finally {'),
        (0, '      this.isLoading = false'),
        (0, '    }'),
        (0, '  }'),
        (0, '}'),
    ]),

    204: dict(title='No Mutations', body=[
        (0, 'Vuex separated synchronous mutations from asynchronous actions so '
            'the devtools could record every state change.'),
        (0, 'Pinia tracks changes through the reactivity system instead, so '
            'the separation is unnecessary.'),
        (0, 'The result: no mutation types, no commit, no string constants — '
            'one less indirection between the component and the state.'),
        (0, '$subscribe and $onAction are still there if you need to observe '
            'changes, for logging or persistence.'),
    ]),

    205: dict(title='Multiple Stores', body=[
        (0, 'Every store is a separate module by construction.'),
        (0, ''),
        (0, 'src/stores/'),
        (0, '  auth.js    -> useAuthStore'),
        (0, '  home.js    -> useHomeStore'),
        (0, ''),
        (0, 'A store can use another store — just call its use-function.'),
        (0, ''),
        (0, "// Vuex needed modules, namespacing, and 'module/action' strings."),
    ]),

    206: dict(title='Pinia and the DevTools', body=[
        (0, 'Vue DevTools shows every registered store'),
        (1, 'Inspect and edit state live'),
        (1, 'A timeline of actions, with arguments and results'),
        (1, 'Time-travel debugging'),
        (0, 'Stores appear as soon as they are first used.'),
    ]),

    207: dict(title='Persisting Store State', body=[
        (0, 'Pinia is extended with plugins.'),
        (0, ''),
        (0, 'pinia.use(({ store }) => {'),
        (0, '  store.$subscribe((_mutation, state) => {'),
        (0, '    localStorage.setItem(store.$id, JSON.stringify(state))'),
        (0, '  })'),
        (0, '})'),
        (0, ''),
        (0, '// pinia-plugin-persistedstate packages this up.'),
    ]),

    208: dict(title='Testing a Store', body=[
        (0, 'A store is a plain function — no component needed.'),
        (0, ''),
        (0, 'beforeEach(() => setActivePinia(createPinia()))'),
        (0, ''),
        (0, "it('increments', () => {"),
        (0, '  const counter = useCounterStore()'),
        (0, ''),
        (0, '  counter.increment()'),
        (0, ''),
        (0, '  expect(counter.count).toBe(1)'),
        (0, '})'),
        (0, ''),
        (0, '// @pinia/testing adds createTestingPinia(), which stubs actions.'),
    ]),

    217: dict(title='Lab 20: Implementing Pinia'),

    # ------------------------------------------------------- Routing (219-223)
    219: dict(title='Creating an SPA with Vue Router', body=[
        (0, 'With Vue Router you map components to routes and tell Vue Router '
            'where to render them.'),
        (0, 'A route component is loaded lazily, so it gets its own bundle.'),
    ]),

    220: dict(title='Vue Router: the Template', body=[
        (0, '<script setup>'),
        (0, "import { RouterLink, RouterView } from 'vue-router'"),
        (0, '</script>'),
        (0, ''),
        (0, '<template>'),
        (0, '  <nav>'),
        (0, '    <RouterLink :to="{ name: \'home\' }">Home</RouterLink>'),
        (0, '    <RouterLink :to="{ name: \'login\' }">Sign in</RouterLink>'),
        (0, '  </nav>'),
        (0, ''),
        (0, '  <RouterView />'),
        (0, '</template>'),
    ]),

    221: dict(title='Vue Router: the JavaScript', body=[
        (0, "import { createRouter, createWebHistory } from 'vue-router'"),
        (0, ''),
        (0, 'export default createRouter({'),
        (0, '  history: createWebHistory(import.meta.env.BASE_URL),'),
        (0, '  routes: ['),
        (0, "    { name: 'home', path: '/',"),
        (0, "      component: () => import('@/components/Home.vue') },"),
        (0, "    { name: 'login', path: '/login',"),
        (0, "      component: () => import('@/components/Login.vue') }"),
        (0, '  ]'),
        (0, '})'),
        (0, ''),
        (0, '// Vue Router 3 wrote new Router({ mode: "history", routes }).'),
    ]),

    223: dict(title='Lab 22: AJAX with Pinia'),
})

REWRITE.update({
    # ------------------------------------------------------ Testing (225-257)
    225: dict(title='Test-Driven Development', body=[
        (0, 'Objectives'),
        (1, 'Learn the TDD steps'),
        (1, 'Write assertions'),
        (1, 'Create tests with Vitest'),
        (1, 'Test components with Vue Test Utils'),
    ]),

    232: dict(body=[
        (0, 'An expression that encapsulates testable logic'),
        (0, 'Assertion styles'),
        (1, "expect(buttonText).toBe('Go!');        // Vitest / Jest"),
        (1, "expect(body).to.be.an('array');        // Chai"),
        (1, 'assert.deepEqual(obj1, obj2);          // node:assert'),
        (0, "Vitest's expect is Chai's, with a Jest-compatible surface."),
    ]),

    233: dict(title='JavaScript Testing Frameworks', body=[
        (0, 'Vitest'),
        (1, 'Vite-native; shares your Vite config and transforms'),
        (0, 'Jest'),
        (1, 'Long the default; needs its own transform setup for Vite projects'),
        (0, 'Mocha + Chai'),
        (1, 'Runner and assertion library, chosen separately'),
        (0, 'node:test'),
        (1, 'Built into Node.js since 18'),
        (0, 'Playwright / Cypress'),
        (1, 'End-to-end, in a real browser'),
    ]),

    235: dict(title='Vitest Overview', body=[
        (0, 'Objectives'),
        (1, 'Learn about the different rendering modes'),
        (1, 'Learn about Vitest'),
        (1, 'Write unit tests with Vitest'),
    ]),

    236: dict(title='Vitest', body=[
        (0, 'The test runner built for Vite'),
        (0, 'Reuses your vite.config.js — aliases, plugins and .vue handling '
            'all work in tests without extra configuration'),
        (0, 'Runs files named *.spec.js or *.test.js'),
        (0, 'Simulates a browser environment with jsdom or happy-dom'),
        (0, 'Jest-compatible API: describe, it, expect, vi.fn()'),
        (0, 'Watch mode re-runs only the tests affected by your last save'),
    ]),

    237: dict(title='How Vitest Works', body=[
        (0, 'Suites describe your tests'),
        (0, 'Specs contain expectations'),
        (0, ''),
        (0, "import { describe, expect, it } from 'vitest'"),
        (0, ''),
        (0, "describe('A suite is just a function', () => {"),
        (0, "  it('and so is a spec', () => {"),
        (0, '    expect(true).toBe(true)'),
        (0, '  })'),
        (0, '})'),
        (0, ''),
        (0, "// Set globals: true in the config to skip the import."),
    ]),

    238: dict(body=[
        (0, 'Created using the describe function'),
        (0, 'Contain one or more specs'),
        (0, '2 params'),
        (1, 'Text description'),
        (1, 'Function'),
        (0, ''),
        (0, "describe('Hello', () => {"),
        (0, '  // ...'),
        (0, '})'),
    ]),

    239: dict(body=[
        (0, 'Created using the it or test function'),
        (1, "they're the same thing"),
        (0, 'Contains one or more expectations'),
        (1, 'expectations === assertions'),
        (0, ''),
        (0, "describe('hello', () => {"),
        (0, "  it('concats Hello and a name', () => {"),
        (0, "    expect(hello('World')).toBe('Hello, World!')"),
        (0, '  })'),
        (0, '})'),
    ]),

    241: dict(body=[
        (0, 'expect(fn).toThrow(e);'),
        (0, 'expect(value).toBe(other);          // Object.is'),
        (0, 'expect(value).toEqual(other);       // deep equality'),
        (0, 'expect(value).toBeDefined();'),
        (0, 'expect(value).toBeTruthy() / .toBeFalsy();'),
        (0, 'expect(number).toBeGreaterThan(n) / .toBeLessThan(n);'),
        (0, 'expect(value).toBeNull() / .toBeUndefined();'),
        (0, 'expect(array).toContain(member);'),
        (0, 'expect(string).toMatch(pattern);'),
        (0, 'await expect(promise).resolves.toBe(value);'),
    ]),

    243: dict(title='TDD Example', body=[
        (0, "describe('Counter', () => {"),
        (0, "  test('tick increases count to 1', () => {"),
        (0, '    const counter = new Counter()'),
        (0, ''),
        (0, '    counter.tick()'),
        (0, ''),
        (0, '    expect(counter.count).toBe(1)'),
        (0, '  })'),
        (0, '})'),
    ]),

    244: dict(title='BDD Example', body=[
        (0, "describe('Counter', () => {"),
        (0, "  it('should increase count by 1 after calling tick', () => {"),
        (0, '    const counter = new Counter()'),
        (0, '    const expected = counter.count + 1'),
        (0, ''),
        (0, '    counter.tick()'),
        (0, ''),
        (0, '    expect(counter.count).toBe(expected)'),
        (0, '  })'),
        (0, '})'),
    ]),

    245: dict(title='Mocking', body=[
        (0, 'vi.fn() — a mock function that records how it was called'),
        (0, 'vi.mock() — replace a whole module'),
        (0, 'vi.spyOn() — wrap an existing method, keeping the original'),
        (0, 'vi.useFakeTimers() — control setTimeout and setInterval'),
        (0, 'vi.stubGlobal() — replace a global such as fetch'),
    ]),

    246: dict(title='Mock Function', body=[
        (0, "import { expect, it, vi } from 'vitest'"),
        (0, ''),
        (0, 'const mockCallback = vi.fn()'),
        (0, ''),
        (0, '[0, 1].forEach(mockCallback)'),
        (0, ''),
        (0, '// The mock function is called twice'),
        (0, 'expect(mockCallback).toHaveBeenCalledTimes(2)'),
        (0, ''),
        (0, '// It was called with 0, and then with 1'),
        (0, 'expect(mockCallback).toHaveBeenNthCalledWith(1, 0, 0, [0, 1])'),
    ]),

    247: dict(title='Mocking a Module', body=[
        (0, 'Replace a module your component imports, so the test never hits '
            'the network.'),
        (0, ''),
        (0, "vi.mock('@/common/api.service', () => ({"),
        (0, '  default: {'),
        (0, '    query: vi.fn().mockResolvedValue({ data: { articles: [] } })'),
        (0, '  }'),
        (0, '}))'),
        (0, ''),
        (0, '// vi.mock is hoisted above the imports, so it applies even'),
        (0, '// though it is written after them.'),
    ]),

    248: dict(title='Resetting Mocks', body=[
        (0, 'Mocks remember every call, so state leaks between tests.'),
        (0, ''),
        (0, 'vi.clearAllMocks()    // forget recorded calls'),
        (0, 'vi.resetAllMocks()    // also drop the implementation'),
        (0, 'vi.restoreAllMocks()  // undo every spyOn'),
        (0, ''),
        (0, '// Or set restoreMocks: true in the Vitest config.'),
    ]),

    249: dict(title='Fake Timers', body=[
        (0, 'vi.useFakeTimers()'),
        (0, ''),
        (0, 'const spy = vi.fn()'),
        (0, 'setTimeout(spy, 5000)'),
        (0, ''),
        (0, 'vi.advanceTimersByTime(5000)'),
        (0, ''),
        (0, 'expect(spy).toHaveBeenCalled()'),
        (0, ''),
        (0, 'vi.useRealTimers()'),
    ]),

    250: dict(title='Snapshot Testing', body=[
        (0, 'Renders a component'),
        (0, 'Writes a snapshot file on the first run'),
        (0, 'Compares later runs against it, and fails if the output differs'),
        (0, 'Update deliberately with vitest -u, and review the diff'),
        (0, 'Best for output that should rarely change; a poor substitute for '
            'an assertion about behaviour'),
    ]),

    251: dict(title='Sample Snapshot Test', body=[
        (0, "it('should render content correctly', () => {"),
        (0, '  const wrapper = mount(Component, {'),
        (0, '    global: { plugins: [pinia, router] }'),
        (0, '  })'),
        (0, ''),
        (0, '  expect(wrapper.html()).toMatchSnapshot()'),
        (0, '})'),
    ]),

    252: dict(title='Vue Test Utils', body=[
        (0, 'The official unit-testing utility library for Vue.'),
        (0, 'Version 2 is the one built for Vue 3.'),
        (0, 'Changes from version 1:'),
        (1, 'propsData is now props'),
        (1, 'createLocalVue is gone — use global.plugins'),
        (1, 'stubs, mocks and provide moved under global'),
        (1, 'setValue and trigger return a promise; await them'),
    ]),

    253: dict(title='mount', body=[
        (0, 'Creates a wrapper containing the mounted and rendered component, '
            'including all of its children.'),
        (0, ''),
        (0, 'const wrapper = mount(Header, {'),
        (0, '  props: { title: \'Conduit\' },'),
        (0, '  global: { plugins: [router] }'),
        (0, '})'),
    ]),

    254: dict(title='shallowMount', body=[
        (0, 'Creates a wrapper containing the mounted and rendered component, '
            'with its child components stubbed out.'),
        (0, 'Useful when a child would fetch data or need its own plugins.'),
        (0, ''),
        (0, 'const wrapper = shallowMount(Home, {'),
        (0, '  global: { plugins: [pinia, router] }'),
        (0, '})'),
    ]),

    255: dict(title='Lab 23: Testing with Vitest'),

    256: dict(title='Testing in a Real Browser'),

    257: dict(title='Browser and End-to-End Testing', body=[
        (0, 'jsdom is a fast approximation of a browser, not a browser.'),
        (0, 'Vitest browser mode runs the same tests in a real one, driven by '
            'Playwright or WebdriverIO.'),
        (0, 'Playwright and Cypress drive the whole application end to end.'),
        (0, 'Karma, which earlier versions of this course covered, was '
            'deprecated in 2023.'),
    ]),

    # -------------------------------------------------- Transitions (258-267)
    259: dict(title='<Transition>', body=[
        (0, 'A built-in wrapper component'),
        (0, 'Creates enter/leave transitions for the element inside it'),
        (0, 'Can be used with:'),
        (1, 'conditional rendering (v-if)'),
        (1, 'conditional display (v-show)'),
        (1, 'dynamic components'),
        (1, 'a component root node'),
        (0, '<TransitionGroup> does the same for a list rendered with v-for'),
    ]),

    260: dict(title='How <Transition> works', body=[
        (0, 'When the wrapped element is inserted or removed...'),
        (0, ''),
        (0, '<button @click="show = !show">Toggle</button>'),
        (0, ''),
        (0, '<Transition name="fade">'),
        (0, '  <p v-if="show">hello</p>'),
        (0, '</Transition>'),
    ]),

    261: dict(title='The transition classes', body=[
        (0, 'Vue looks for CSS transitions or animations named after the '
            'transition\'s name attribute, and applies these classes in order:'),
        (1, 'v-enter-from — the starting state, applied before insertion'),
        (1, 'v-enter-active — applied for the whole entering phase'),
        (1, 'v-enter-to — the end state of the enter transition'),
        (1, 'v-leave-from — the starting state of the leave transition'),
        (1, 'v-leave-active — applied for the whole leaving phase'),
        (1, 'v-leave-to — the end state, applied until the animation finishes'),
        (0, 'Vue 2 called the first and fourth v-enter and v-leave. Renaming '
            'them is the most common reason an old example stops animating.'),
    ]),

    262: dict(title='Defining the CSS', body=[
        (0, '.fade-enter-active,'),
        (0, '.fade-leave-active {'),
        (0, '  transition: all 0.3s ease;'),
        (0, '}'),
        (0, ''),
        (0, '.fade-enter-from,'),
        (0, '.fade-leave-to {'),
        (0, '  transform: translateX(10px);'),
        (0, '  opacity: 0;'),
        (0, '}'),
    ]),

    263: dict(title='JavaScript hooks', body=[
        (0, '<Transition'),
        (0, '  @before-enter="beforeEnter"'),
        (0, '  @enter="enter"'),
        (0, '  @after-enter="afterEnter"'),
        (0, '  @enter-cancelled="enterCancelled"'),
        (0, '  @before-leave="beforeLeave"'),
        (0, '  @leave="leave"'),
        (0, '  @after-leave="afterLeave"'),
        (0, '  @leave-cancelled="leaveCancelled"'),
        (0, '  :css="false"'),
        (0, '>'),
        (0, '  <p v-if="show">hello</p>'),
        (0, '</Transition>'),
    ]),

    264: dict(title='Using the JavaScript hooks', body=[
        (0, 'Declare the handlers in <script setup>.'),
        (0, ''),
        (0, 'function beforeEnter(el) {'),
        (0, '  el.style.opacity = 0'),
        (0, '}'),
        (0, ''),
        (0, 'function enter(el, done) {'),
        (0, '  // call done() when the animation finishes'),
        (0, '  done()'),
        (0, '}'),
        (0, ''),
        (0, '// Set :css="false" so Vue does not also wait for CSS.'),
    ]),

    265: dict(title='Custom Transition Classes', body=[
        (0, 'Override the generated class names to plug in a CSS animation '
            'library:'),
        (1, 'enter-from-class'),
        (1, 'enter-active-class'),
        (1, 'enter-to-class'),
        (1, 'leave-from-class'),
        (1, 'leave-active-class'),
        (1, 'leave-to-class'),
        (0, 'Vue 2 named the first and fourth enter-class and leave-class.'),
    ]),

    266: dict(title='Custom Transition Classes Example', body=[
        (0, '<link'),
        (0, '  href="https://cdn.jsdelivr.net/npm/animate.css@4.1.1"'),
        (0, '  rel="stylesheet">'),
        (0, ''),
        (0, '<Transition'),
        (0, '  enter-active-class="animate__animated animate__tada"'),
        (0, '  leave-active-class="animate__animated animate__bounceOutRight"'),
        (0, '>'),
        (0, '  <p v-if="show">hello</p>'),
        (0, '</Transition>'),
    ]),
})

# Slides with no Vue 3 equivalent. 1-based numbers in the v1.5 deck.
DELETE = [
    105,  # Using Filters — filters were removed in Vue 3
    106,  # Formatting Currencies with Filters
    107,  # Formatting Dates with Filters
    189,  # Custom Option Merge Strategies — mixin internals
    209,  # Object-style Commit — Vuex only
    210,  # Committing Mutations in Components — Vuex only
    211,  # Async Mutations with Actions — Vuex only
    212,  # Actions vs. Mutations — Pinia has no mutations
    213,  # Registering Actions — Vuex only
    214,  # Dispatching Actions — Vuex only
    215,  # Composing Actions — Vuex only
    216,  # Splitting the Store with Modules — Pinia stores are modules
]

# New slides, inserted after the given v1.5 slide number.
INSERT = [
    # (after this v1.5 slide number, order within that anchor, layout, title, body)
    (28, 1, 'Title and Content', 'Single-File Components', [
        (0, '<script setup>   - the logic, using the Composition API'),
        (0, '<template>       - the markup'),
        (0, '<style scoped>   - CSS that applies to this component only'),
        (0, ''),
        (0, 'One file, one component, named after the file.'),
        (0, 'Compiled at build time, so the format costs nothing at runtime.'),
    ]),
    (85, 1, 'Title and Content', 'Options API vs. Composition API', [
        (0, 'Options API'),
        (1, 'Code is grouped by option: data, computed, methods, watch'),
        (1, 'A single feature is spread across several options'),
        (1, 'Reuse means mixins'),
        (0, 'Composition API'),
        (1, 'Code is grouped by feature'),
        (1, 'Reuse means composables - ordinary functions'),
        (1, 'Better type inference and IDE support'),
        (0, 'Both are fully supported. This course uses the Composition API, '
            'which is what current Vue code is written with.'),
    ]),
    (86, 1, 'Title and Content', '<script setup>', [
        (0, '<script setup>'),
        (0, "import { computed, ref } from 'vue'"),
        (0, "import ArticleList from './ArticleList.vue'   // and registered"),
        (0, ''),
        (0, 'const count = ref(0)                          // state'),
        (0, 'const doubled = computed(() => count.value * 2)'),
        (0, ''),
        (0, 'function increment() { count.value++ }        // behaviour'),
        (0, '</script>'),
        (0, ''),
        (0, '// Every top-level binding is available to the template.'),
        (0, '// No export default, no components object, no `this`.'),
    ]),
    (86, 2, 'Title and Content', 'ref and computed', [
        (0, 'ref(value) wraps any value in a reactive container'),
        (1, 'Read and write it as .value in script'),
        (1, 'Vue unwraps it for you in the template'),
        (0, 'computed(getter) derives a cached, read-only value'),
        (1, 'Re-evaluates only when something it read has changed'),
        (0, 'reactive(object) makes an object reactive without .value'),
        (1, 'Objects only, and it does not survive destructuring'),
        (0, 'Reach for ref by default.'),
    ]),
    (86, 3, 'Title and Content', 'Compiler Macros', [
        (0, 'Available only at the top level of <script setup>. They are not '
            'imported - the compiler handles them.'),
        (0, ''),
        (0, 'defineProps({ ... })       - declare the props'),
        (0, "defineEmits(['change'])    - declare the events"),
        (0, 'defineModel()              - a writable v-model ref (3.4+)'),
        (0, 'defineExpose({ ... })      - expose members to a template ref'),
        (0, 'defineOptions({ ... })     - set component options such as name'),
    ]),
]

REWRITE.update({
    79: dict(title='Manipulating HTML With Vue.js', body=[
        (0, '<div id="favoriteSongs">'),
        (0, '  <ol>'),
        (0, '    <li v-for="song in songs" :key="song.title" class="song">'),
        (0, '      {{ song.title }}'),
        (0, '    </li>'),
        (0, '  </ol>'),
        (0, '</div>'),
        (0, ''),
        (0, "import { createApp } from 'vue'"),
        (0, ''),
        (0, 'createApp({'),
        (0, '  data() {'),
        (0, '    return {'),
        (0, '      songs: ['),
        (0, "        { title: 'Walk This Way' },"),
        (0, "        { title: 'Give It Away' },"),
        (0, "        { title: 'My Way' }"),
        (0, '      ]'),
        (0, '    }'),
        (0, '  }'),
        (0, "}).mount('#favoriteSongs')"),
    ]),

    78: dict(title='Manipulating HTML with React', body=[
        (0, '<div id="favoriteSongs"></div>'),
        (0, ''),
        (0, 'function FavoriteSongs({ song }) {'),
        (0, '  return ('),
        (0, '    <ol>'),
        (0, '      <li className="song">{song}</li>'),
        (0, '    </ol>'),
        (0, '  );'),
        (0, '}'),
        (0, ''),
        (0, "createRoot(document.getElementById('favoriteSongs'))"),
        (0, '  .render(<FavoriteSongs song="My New Favorite Song" />);'),
    ]),
})

REWRITE.update({
    22: dict(title='Code Editors and IDEs', body=[
        (0, 'Visual Studio Code'),
        (1, 'With the Vue - Official extension'),
        (0, 'JetBrains WebStorm / IntelliJ IDEA'),
        (0, 'Zed'),
        (0, 'Sublime Text'),
        (0, 'Neovim / Emacs'),
        (0, 'Any editor with a Volar language-server client will do.'),
    ]),
    56: dict(title='Static Code Analysis', body=[
        (0, 'Objectives'),
        (1, 'Learn about lint tools'),
        (1, 'Use ESLint'),
        (1, 'Configure ESLint with a flat config'),
        (1, 'Manual testing with a local dev server'),
    ]),
    68: dict(title='The Document Object Model'),
    268: dict(title='ES2015 (ES6) and Beyond'),
    57: dict(title='Lint tools', body=[
        (0, 'ESLint'),
        (1, 'The standard. Pluggable, and "agenda free" - it does not push a '
            'particular style'),
        (1, 'Flat config (eslint.config.js) since version 9'),
        (0, 'Biome'),
        (1, 'Linter and formatter in one, written in Rust'),
        (0, 'oxlint'),
        (1, 'A very fast linter, also Rust; often run alongside ESLint'),
        (0, 'Prettier'),
        (1, 'A formatter, not a linter - it is about layout, not correctness'),
        (0, 'JSLint and JSHint came first, and are now rarely used.'),
    ]),
})
