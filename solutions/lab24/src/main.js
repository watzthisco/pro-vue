import Vue from 'vue'
import App from './App.vue'
import ApiService from "./common/api.service";
import store from "./store";
import router from "./router";

ApiService.init();
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
