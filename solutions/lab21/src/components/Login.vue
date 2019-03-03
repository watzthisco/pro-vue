<template>
  <div>
    <h1>Log In Here</h1>
    <form v-on:submit.prevent="onSubmit();">
        <fieldset class="form-group">
            <input
            class="form-control form-control-lg"
            type="text"
            placeholder="Email"
            />
        </fieldset>
        <fieldset class="form-group">
            <input
            class="form-control form-control-lg"
            type="password"
            placeholder="Password"
            />
        </fieldset>
        <button class="btn btn-lg btn-primary pull-xs-right">
            Sign in
        </button>
    </form>
    </div>
</template>


<script>

export default {
    name: 'Login',
    components: {
      
    }
}
</script>
<style></style>