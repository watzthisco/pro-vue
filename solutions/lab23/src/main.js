import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import ApiService from './common/api.service';
import router from './router';

ApiService.init();

const app = createApp(App);

// Pinia must be installed before the router so that navigation guards and
// route components can reach the stores.
app.use(createPinia());
app.use(router);
app.mount('#app');
