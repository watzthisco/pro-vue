const { createApp } = Vue;

createApp({
  data() {
    return {
      firstName: 'Joe',
      lastName: 'Talcum',
    };
  },
  computed: {
    computeFullName() {
      return `${this.firstName} ${this.lastName}`;
    },
  },
}).mount('#app');
