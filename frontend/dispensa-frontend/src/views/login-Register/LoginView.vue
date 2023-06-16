<template>
  <!-- component -->
  <div class="min-h-screen bg-gray-100 flex flex-col sm:py-12">
    <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
      <!-- alert dati errati -->
      <div v-show="show_alert"
        class="flex p-4 mb-4 text-sm text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800"
        role="alert">
        <svg aria-hidden="true" class="flex-shrink-0 inline w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
            clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Info</span>
        <div>
          <span class="font-medium">Login fallito!</span> {{ this.testo_alert }}
        </div>
      </div>
      <div v-show="!authStore.isAuthenticated">
        <!-- Login -->
        <h1 class="font-bold text-center text-2xl mb-5">Esegui il login</h1>
        <div class="bg-white shadow w-full rounded-lg divide-y divide-gray-200 dark:bg-slate-800">
          <div class="px-5 py-3 pt-6 ">
            <label class="font-semibold text-sm text-gray-600 pb-1 block dark:text-white">Username</label>
            <input v-model="this.username" type="text"
              class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full dark:text-slate-800" />
            <label class="font-semibold text-sm text-gray-600 pb-1 block dark:text-white">Password</label>
            <input v-model="password" type="password"
              class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full dark:text-slate-800" />
            <button @click="login" type="button"
              class="w-full bg-indigo-500 text-white text-sm font-bold py-2 px-4 rounded-md hover:bg-indigo-600 transition duration-300">
              <span class="inline-block mr-2">Login</span>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                class="w-4 h-4 inline-block">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </button>
            <div class="flex items-start mt-4 mb-1">

              <label for="terms" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Non hai un account?
                <router-link :to="{ name: 'register' }"><a href="#"
                    class="text-blue-600 hover:underline dark:text-blue-500">Registrati!</a>
                </router-link>
              </label>
            </div>
          </div>
          <div class="p-4">
            <div class="grid grid-cols-3 gap-1">
              <button type="button"
                class="transition duration-200 border border-gray-200 text-gray-500 w-full py-2.5 rounded-lg text-sm shadow-sm hover:shadow-md font-normal text-center inline-block dark:text-white">MailUp</button>
              <button type="button"
                class="transition duration-200 border border-gray-200 text-gray-500 w-full py-2.5 rounded-lg text-sm shadow-sm hover:shadow-md font-normal text-center inline-block dark:text-white">Google</button>
              <button type="button"
                class="transition duration-200 border border-gray-200 text-gray-500 w-full py-2.5 rounded-lg text-sm shadow-sm hover:shadow-md font-normal text-center inline-block dark:text-white">Github</button>
            </div>
          </div>
          <div class="py-5">
            <div class="grid grid-cols-2 gap-1">
              <div class="text-center sm:text-left whitespace-nowrap">
                <button
                  class="transition duration-200 mx-5 px-5 py-4 cursor-pointer font-normal text-sm rounded-lg text-gray-500 hover:bg-gray-100 focus:outline-none focus:bg-gray-200 focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 ring-inset">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    class="w-4 h-4 inline-block align-text-top">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z" />
                  </svg>
                  <span class="inline-block ml-1 dark:text-white">Forgot Password</span>
                </button>
              </div>
              <div class="text-center sm:text-right whitespace-nowrap">
                <button
                  class="transition duration-200 mx-5 px-5 py-4 cursor-pointer font-normal text-sm rounded-lg text-gray-500 hover:bg-gray-100 focus:outline-none focus:bg-gray-200 focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 ring-inset">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    class="w-4 h-4 inline-block align-text-bottom	">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
                  </svg>
                  <span class="inline-block ml-1 dark:text-white">Help</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="py-5">
        <div class="grid grid-cols-2 gap-1">
          <div class="text-center sm:text-left whitespace-nowrap">
            <button
              class="transition duration-200 mx-5 px-5 py-4 cursor-pointer font-normal text-sm rounded-lg text-gray-500 hover:bg-gray-200 focus:outline-none focus:bg-gray-300 focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 ring-inset">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                class="w-4 h-4 inline-block align-text-top">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              <router-link :to="{ name: 'home' }">
                <span class="inline-block ml-1">Back to Dispensa Digitale</span>
              </router-link>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from '@/router/index'
import { useAuthStore } from '@/stores/auth'


export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: 'Login',
  components: {

  },
  data() {
    return {
      username: '',
      password: '',
      show_alert: false,
      testo_alert: ''
    }
  },
  methods: {
    async login() {
      this.authStore.login(this.username, this.password).then(res => {
        if (res) {
          console.log("login ok")
          router.push({ name: 'home' });
        }
        else{
          console.log("login fail")
          this.testo_alert = 'Controlla i dati inseriti, Si fa distinzione tra maiuscole e minuscole!'
          this.show_alert = true
        }
      })

    }
  },
  beforeMount() {
    if (this.authStore.isAuthenticated){
      this.testo_alert = 'Sei gia autenticato, esegui il logout prima!'
      this.show_alert = true
    }
  },
  
  
}
</script>