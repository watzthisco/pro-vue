import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import ApiService from './common/api.service'
ApiService.init()

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')
