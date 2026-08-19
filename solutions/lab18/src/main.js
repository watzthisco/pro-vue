import { createApp } from 'vue';

import App from './App.vue';
import ApiService from './common/api.service';
import './assets/app.css';

ApiService.init();

createApp(App).mount('#app');
