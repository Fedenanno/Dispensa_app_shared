import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

//store di autenticazione
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory('/'), //import.meta.env.BASE_URL
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login-Register/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/login-Register/RegisterView.vue')
    },
    {
      path: '/nuovaDispensa',
      name: 'nuovaDispensa',
      component: () => import('../views/dispense/nuovaDispensaView.vue')
    },
    {
      path: '/dispenseHome/:id',
      name: 'dispenseHome',
      component: () => import('../views/dispense/dispensaHomeView.vue'),
      props: true
    },
    {
      path: '/prova/:id',
      name: 'prova',
      component: () => import('../views/prova.vue'),
      props: true
    },
    {
      path: '/offllineView',
      name: 'offllineView',
      component: () => import('../views/offllineView.vue'),
    }
  ]
})

//routerguard per preventivo accesso a pagine non autorizzate
router.beforeEach(async (to, from) => {
  if (!navigator.onLine && to.path !== '/offllineView') {
    // Se l'app è offline, reindirizza verso la pagina offline
    return { name: 'offllineView' }
  }
  const store = await useAuthStore()
  //se non è autenticato e non sta andando alla pagina di login, lo rimando io alla pagina di login
  if (!store.isAuthenticated && to.name !== 'login' && to.name !== 'register' && to.name !== 'home') {
    // redirect the user to the login page
    return { name: 'login' }
  }
})

export default router
