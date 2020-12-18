import Vue from 'vue'
import App from './App.vue'
import ApiService from "./common/api.service";
import './assets/app.css'

ApiService.init();
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
