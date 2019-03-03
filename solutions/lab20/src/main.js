import Vue from 'vue'
import App from './App.vue'
import ApiService from "./common/api.service";
import store from "./store";

ApiService.init();
Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
