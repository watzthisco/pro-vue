import { createRouter, createWebHistory } from 'vue-router'

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('@/components/HomeContent.vue'),
      children: [
        {
          name: 'home',
          path: '',
          component: () => import('@/components/GlobalFeed.vue'),
        },
        {
          name: 'popular',
          path: 'popular',
          component: () => import('@/components/PopularFeed.vue'),
        },
      ],
    },
    {
      name: 'login',
      path: '/login',
      component: () => import('@/components/LoginPage.vue'),
    },
    {
      name: 'register',
      path: '/register',
      component: () => import('@/components/SignUpPage.vue'),
    },
  ],
})
