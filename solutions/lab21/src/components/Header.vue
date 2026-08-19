<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <nav class="navbar">
    <div class="container">
      <RouterLink class="navbar-brand" :to="{ name: 'home' }">Logo</RouterLink>
      <ul class="nav navbar-nav flex-row">
        <li class="nav-item p-2">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'home' }">
            Home
          </RouterLink>
        </li>
        <li class="nav-item p-2">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'login' }">
            Sign in
          </RouterLink>
        </li>
        <li class="nav-item p-2">
          <a class="nav-link">Sign Up</a>
        </li>
      </ul>
    </div>
  </nav>
</template>
