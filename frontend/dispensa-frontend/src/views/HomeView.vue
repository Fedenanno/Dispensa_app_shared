<template>
  <div class="md:container md:mx-auto">

    <!-- In caso di login -->
    <!-- v-if="this.authStore.isAuthenticated()" -->
    <div v-show="authStore.user">
      <div class="grid gap-4 grid-cols-3 grid-rows-3 pt-6">

        <!-- dispense dell'utente -->
        <div v-for="dispensa in this.dispense">
          <!-- <router-link :to="{ name: 'dispenseHome', params: { id : dispensa.id_dispensa}}"> -->
          <div @click="apriDispensa(dispensa.id_dispensa)" class="bg-white dark:bg-slate-800 rounded-lg hover:bg-indigo-100 px-6 py-8 ring-1 ring-slate-900/5 shadow-xl">
            
            <div>
              <span class="inline-flex items-center justify-center p-2 bg-indigo-500 rounded-md shadow-lg">
                <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor" aria-hidden="true"></svg>
              </span>
            </div>
            <h3 class="text-slate-900 dark:text-white mt-5 text-base font-medium tracking-tight">{{ dispensa.nome_dispensa
            }}</h3>
            <p class="text-slate-500 dark:text-slate-400 mt-2 text-sm">
              The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer
              space.
            </p>
          </div>
        <!-- </router-link> -->
        </div>

        <div @click="this.nuovaDipensa" class="bg-white dark:bg-slate-800 hover:bg-indigo-100 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl">
          <div>
            <span class="inline-flex items-center justify-center p-2 bg-indigo-500 rounded-md shadow-lg">
              <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" aria-hidden="true"></svg>
            </span>
          </div>
          <h3 class="text-slate-900 dark:text-white mt-5 text-base font-medium tracking-tight">Nuova Dispensa</h3>
          <p class="text-slate-500 dark:text-slate-400 mt-2 text-sm">
            Crea una nuova dispensa!
          </p>
        </div>
        
      </div>
    </div>

    <!-- se l'utente non è loggato -->
    <div>

    </div>

    <!-- In caso di logout -->
  </div>
</template>


<script>
import { axios } from '@/common/axiosSetting'
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
      dispense: [],
    }
  },
  methods: {
    async getDispense() {
      const response = await axios.get('dispense/')
      this.dispense = response.data

    },
    nuovaDipensa(){
      router.push({ name: 'nuovaDispensa' });
    },
    apriDispensa(dispensa){
      router.push({ name: 'prova', params: { id: dispensa } });
    }

  },

  beforeMount() {
    if(this.authStore.isAuthenticated)
      this.getDispense()
  },
  
}

</script>




<!-- 
<div class="bg-white dark:bg-slate-800 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl">
        <div>
          <span class="inline-flex items-center justify-center p-2 bg-indigo-500 rounded-md shadow-lg">
            <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
              stroke="currentColor" aria-hidden="true"></svg>
          </span>
        </div>
        <h3 class="text-slate-900 dark:text-white mt-5 text-base font-medium tracking-tight">Writes Upside-Down</h3>
        <p class="text-slate-500 dark:text-slate-400 mt-2 text-sm">
          The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer
          space.
        </p>
      </div> -->