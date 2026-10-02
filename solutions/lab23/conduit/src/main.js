import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import ApiService from './common/api.service'
import { useAuthStore } from './stores/auth'
ApiService.init()

const app = createApp(App)

app.use(createPinia())
useAuthStore().checkAuth()
app.use(router)
app.mount('#app')
