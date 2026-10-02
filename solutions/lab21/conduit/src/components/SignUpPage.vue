<script setup>
// The form is wired up to the auth store in the next lab.
function onSubmit() {}
</script>

<template>
  <div>
    <h1>Sign Up Here</h1>
    <form @submit.prevent="onSubmit">
      <fieldset class="form-group">
        <input class="form-control form-control-lg" type="text" placeholder="Username" />
      </fieldset>
      <fieldset class="form-group">
        <input class="form-control form-control-lg" type="text" placeholder="Email" />
      </fieldset>
      <fieldset class="form-group">
        <input class="form-control form-control-lg" type="password" placeholder="Password" />
      </fieldset>
      <button class="btn btn-lg btn-primary pull-xs-right">Sign up</button>
    </form>
  </div>
</template>
