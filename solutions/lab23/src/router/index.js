import { createRouter, createWebHistory } from 'vue-router';

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'home',
      path: '/',
      component: () => import('@/components/Home.vue'),
    },
    {
      name: 'login',
      path: '/login',
      component: () => import('@/components/Login.vue'),
    },
    {
      name: 'register',
      path: '/register',
      component: () => import('@/components/Register.vue'),
    },
  ],
});
