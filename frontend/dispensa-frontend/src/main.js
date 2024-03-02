import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import '@/common/axiosSetting'

import { useAuthStore } from '@/stores/auth'

//Componente per il datepicker
import VueTailwindDatepicker from 'vue-tailwind-datepicker'
//Componente per le notifiche grafiche
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';


//vue config
const app = createApp(App)

//store per autenticazione
const pinia = createPinia()
app.use(pinia)
const store = useAuthStore()

app.use(router)

//css config
app.use(VueTailwindDatepicker)
app.use(ToastPlugin)

app.mount('#app')
