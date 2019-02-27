
new Vue({
  el:"#app",
  data: {
    firstName: 'Joe',
    lastName: 'Talcum'
  },
  methods: {
    
  },
  computed: {
    computeFullName: function(){
      return this.firstName + ' ' + this.lastName;
    }
    
    
    
  }
})