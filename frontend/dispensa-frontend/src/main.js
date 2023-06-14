import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import '@/common/axiosSetting'

import { useAuthStore } from '@/stores/auth'


const app = createApp(App)

app.use(createPinia())
const authStore = await useAuthStore();

app.use(router)

app.mount('#app')
