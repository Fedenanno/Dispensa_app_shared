import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
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
    }
  ]
})

export default router
