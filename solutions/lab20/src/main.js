import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import ApiService from './common/api.service';

ApiService.init();

const app = createApp(App);

app.use(createPinia());
app.mount('#app');
