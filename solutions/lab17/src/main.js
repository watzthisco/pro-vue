import { createApp } from 'vue';

import App from './App.vue';
import ApiService from './common/api.service';

ApiService.init();

createApp(App).mount('#app');
