const { createApp, ref } = Vue;

createApp({
  setup() {
    // Only ever render trusted HTML with v-html: it is an XSS vector.
    const rawHtml = ref('<span style="color:red">This should be red.</span>');

    return { rawHtml };
  },
}).mount('#app');
