const { createApp } = Vue;

createApp({
  data() {
    return {
      // Only ever render trusted HTML with v-html: it is an XSS vector.
      rawHtml: '<span style="color:red">This should be red.</span>',
    };
  },
}).mount('#app');
