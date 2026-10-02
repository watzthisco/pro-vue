<script setup>
import { storeToRefs } from 'pinia'
import { RouterLink, useRouter } from 'vue-router'

import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const { isAuthenticated } = storeToRefs(authStore)

function logout() {
  authStore.logout()
  router.push({ name: 'home' })
}
</script>

<template>
  <nav class="navbar">
    <div class="container">
      <RouterLink class="navbar-brand" :to="{ name: 'home' }">Conduit</RouterLink>
      <ul class="nav navbar-nav flex-row">
        <li class="nav-item p-2">
          <RouterLink class="nav-link" exact-active-class="active" :to="{ name: 'home' }">
            Home
          </RouterLink>
        </li>

        <li v-if="isAuthenticated" class="nav-item p-2">
          <a class="nav-link" href="#" @click.prevent="logout">Log out</a>
        </li>
        <template v-else>
          <li class="nav-item p-2">
            <RouterLink class="nav-link" active-class="active" :to="{ name: 'login' }">
              Sign In
            </RouterLink>
          </li>
          <li class="nav-item p-2">
            <RouterLink class="nav-link" active-class="active" :to="{ name: 'register' }">
              Sign Up
            </RouterLink>
          </li>
        </template>
      </ul>
    </div>
  </nav>
</template>
