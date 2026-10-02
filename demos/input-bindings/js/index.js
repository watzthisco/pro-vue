const { createApp, ref, computed } = Vue;

createApp({
  setup() {
    const firstName = ref('Joe');
    const lastName = ref('Talcum');

    const computeFullName = computed(() => `${firstName.value} ${lastName.value}`);

    return { firstName, lastName, computeFullName };
  },
}).mount('#app');
