<template>



  <navbar />
        <!-- <RouterLink to="/about">About</RouterLink> -->
  

  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import navbar from '@/components/navbar.vue'
import { useAuthStore } from '@/stores/auth'

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: 'App',
  components: {
    navbar,
  },
  beforeCreate() {
    //inizializza lo store
    console.log("inizializzo user")
    this.authStore.getUser();
  },
}

</script>

<style scoped>


</style>
