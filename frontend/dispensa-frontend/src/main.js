import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import '@/common/axiosSetting'

import { useAuthStore } from '@/stores/auth'

import VueTailwindDatepicker from 'vue-tailwind-datepicker'

//vue config
const app = createApp(App)

//store per autenticazione
const pinia = createPinia()
app.use(pinia)
const store = useAuthStore()


app.use(router)



//css config
app.use(VueTailwindDatepicker)

app.mount('#app')
