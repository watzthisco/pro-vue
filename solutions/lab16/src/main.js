import Vue from 'vue'
import App from './App.vue'
import ApiService from "./common/api.service";

Vue.config.productionTip = false
ApiService.init();
new Vue({
  render: h => h(App),
}).$mount('#app')
