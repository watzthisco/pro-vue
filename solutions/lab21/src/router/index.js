import { createRouter, createWebHistory } from 'vue-router';

// createWebHistory replaces `mode: 'history'` from Vue Router 3.
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
  ],
});
