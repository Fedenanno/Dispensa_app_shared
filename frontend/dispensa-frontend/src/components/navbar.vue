<template>
  <!-- component -->
  <nav class="flex dark:bg-slate-900 items-center relative justify-between bg-white px-5 py-6 w-full">

    <!-- icona -->
    <div>
      <svg width="41" height="39" viewBox="0 0 41 39" fill="none" xmlns="http://www.w3.org/2000/svg">
      </svg>
    </div>
    <!-- Pulsanti -->
    <ul id="drawer" role="menu"
      class="sm:gap-3 transition-left ease-[cubic-bezier(0.4, 0.0, 0.2, 1)] delay-150  sm:flex  flex flex-col cursor-pointer absolute min-h-screen -left-48 sm:static w-48 top-0 bg-white sm:shadow-none shadow-xl sm:bg-transparent sm:flex-row sm:w-auto sm:min-h-0 dark:bg-slate-900  ">

      <li
        class="font-medium text-sm p-3 hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-primary">
        <router-link :to="{ name: 'home'}">
          <a href="#" class="dark:text-white">Home</a>
        </router-link>
      </li>
      <!-- <li
        class="font-medium text-sm p-3 cursor-pointer hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-gray-600 hover:text-primary transition-colors">
        <a href="#" class="dark:text-white">Women</a>
      </li>
      <li
        class="font-medium text-sm p-3 cursor-pointer hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-gray-600 hover:text-primary transition-colors">
        <a href="#" class="dark:text-white">Kids</a>
      </li> -->
    </ul>

    <div class="flex gap-3 items-center">
      <!-- Icona carrello -->
      <!-- <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path class="dark:fill-white" fill-rule="evenodd" clip-rule="evenodd"
          d="M16.9303 7C16.9621 6.92913 16.977 6.85189 16.9739 6.77432H17C16.8882 4.10591 14.6849 2 12.0049 2C9.325 2 7.12172 4.10591 7.00989 6.77432C6.9967 6.84898 6.9967 6.92535 7.00989 7H6.93171C5.65022 7 4.28034 7.84597 3.88264 10.1201L3.1049 16.3147C2.46858 20.8629 4.81062 22 7.86853 22H16.1585C19.2075 22 21.4789 20.3535 20.9133 16.3147L20.1444 10.1201C19.676 7.90964 18.3503 7 17.0865 7H16.9303ZM15.4932 7C15.4654 6.92794 15.4506 6.85153 15.4497 6.77432C15.4497 4.85682 13.8899 3.30238 11.9657 3.30238C10.0416 3.30238 8.48184 4.85682 8.48184 6.77432C8.49502 6.84898 8.49502 6.92535 8.48184 7H15.4932ZM9.097 12.1486C8.60889 12.1486 8.21321 11.7413 8.21321 11.2389C8.21321 10.7366 8.60889 10.3293 9.097 10.3293C9.5851 10.3293 9.98079 10.7366 9.98079 11.2389C9.98079 11.7413 9.5851 12.1486 9.097 12.1486ZM14.002 11.2389C14.002 11.7413 14.3977 12.1486 14.8858 12.1486C15.3739 12.1486 15.7696 11.7413 15.7696 11.2389C15.7696 10.7366 15.3739 10.3293 14.8858 10.3293C14.3977 10.3293 14.002 10.7366 14.002 11.2389Z"
          fill="#200E32" />
      </svg> -->


      <div v-show="authStore.isAuthenticated" @click="showMenu = !showMenu"
        class="h-10 w-10 hover:ring-4 user cursor-pointer relative ring-blue-700/30 rounded-full bg-cover bg-center bg-[url('https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80')]">
        <!-- Menu a tentida utente loggato-->
        <div v-if="showMenu" class="drop-down  w-48 overflow-hidden bg-white rounded-md shadow absolute top-12 right-3">
          <ul>
            <!-- Impostazioni -->
            <li class="px-3 py-3 text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
              </span>
              <span> Impostazioni </span>
            </li>
            <!-- Account -->
            <li class="px-3  py-3  text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </span>
              <span> Account </span>
            </li>
            <!-- Notifiche On -->
            <li v-if="this.statoNotifiche" class="px-3  py-3  text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </span>
              <span> Notifiche On </span>
            </li>
            <!-- Notifiche Off -->
            <li v-else @click="this.abilitaNotifiche()" class="px-3  py-3  text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </span>
              <span> Abilita notifiche </span>
            </li>
            <!-- Logout -->
            <li @click="this.logout"
              class="px-3  py-3 text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
              </span>
              <span> Logout </span>
            </li>
          </ul>
        </div>
      </div>

      <!-- in caso di utente non loggato, mostro il pulsante login -->
      <div v-show="!authStore.isAuthenticated">
        <button @click="this.$router.push({ name: 'login' })"
          class="block text-white bg-indigo-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-blue-800">Login</button>
      </div>


      <div class="sm:hidden cursor-pointer" id="mobile-toggle">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path class="dark:stroke-white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </div>
    </div>
  </nav>
</template>

<script>
import { useAuthStore } from '@/stores/auth'
import router from '@/router/index'

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  data() {
    return {
      showMenu: false,
      statoNotifiche: false,
    }
  },
  methods: {
    logout() {
      console.log("logout from navbar");
      if (this.authStore.isAuthenticated) {
        this.authStore.logout();
        router.push({ name: 'home' });
      }
    },
    randomNotification() {
      console.log('notifica random')
      const notifTitle = 'Notifiche Dispensa';
      const notifBody = `Notifiche abilitate con successo!`;
      const notifImg = `/icon_pwa/512_icon.png`;
      const options = {
        body: notifBody,
        icon: notifImg,
      };
      new Notification(notifTitle, options);
      //setTimeout(this.randomNotification, 30000);
    },

    abilitaNotifiche(){
      Notification.requestPermission().then((result) => {
        if (result === "granted") {
          console.log('notifiche abilitate')
          this.statoNotifiche = true;
          this.randomNotification();
        }
      });
    },

  },
  mounted() {
    this.statoNotifiche = Notification.permission === "granted"
  }
}

</script>