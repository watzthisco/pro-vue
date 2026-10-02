<script setup>
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { RouterLink, useRouter } from 'vue-router';

import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const authStore = useAuthStore();
const { errors } = storeToRefs(authStore);

const username = ref('');
const email = ref('');
const password = ref('');

async function onSubmit() {
  try {
    await authStore.register({
      email: email.value,
      password: password.value,
      username: username.value,
    });
    router.push({ name: 'home' });
  } catch {
    // Errors are surfaced through the store's `errors` state.
  }
}
</script>

<template>
  <div class="auth-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-6 offset-md-3 col-xs-12">
          <h1 class="text-xs-center">Sign up</h1>
          <p class="text-xs-center">
            <RouterLink :to="{ name: 'login' }">Have an account?</RouterLink>
          </p>
          <ul v-if="errors" class="error-messages">
            <li v-for="(messages, field) in errors" :key="field">
              {{ field }} {{ Array.isArray(messages) ? messages.join(', ') : messages }}
            </li>
          </ul>
          <form @submit.prevent="onSubmit">
            <fieldset class="form-group">
              <input
                v-model="username"
                class="form-control form-control-lg"
                type="text"
                placeholder="Username"
              />
            </fieldset>
            <fieldset class="form-group">
              <input
                v-model="email"
                class="form-control form-control-lg"
                type="text"
                placeholder="Email"
              />
            </fieldset>
            <fieldset class="form-group">
              <input
                v-model="password"
                class="form-control form-control-lg"
                type="password"
                placeholder="Password"
              />
            </fieldset>
            <button class="btn btn-lg btn-primary pull-xs-right">Sign up</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
