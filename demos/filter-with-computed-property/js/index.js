const PEOPLE = [
  { name: 'Ping', age: 20 },
  { name: 'Amir', age: 24 },
  { name: 'Shabnum', age: 30 },
  { name: 'Mark', age: 40 },
];

const { createApp } = Vue;

createApp({
  data() {
    return {
      searchDetails: '',
      sortKey: 'name',
      reverse: false,
      people: PEOPLE,
    };
  },
  computed: {
    // A computed property is cached: it only re-runs when one of the
    // reactive values it reads actually changes.
    filterIt() {
      const term = this.searchDetails.trim().toLowerCase();

      const matches = this.people.filter(
        (person) =>
          person.name.toLowerCase().includes(term) ||
          String(person.age).includes(term),
      );

      const direction = this.reverse ? -1 : 1;

      return [...matches].sort((a, b) => {
        const left = a[this.sortKey];
        const right = b[this.sortKey];

        if (left === right) return 0;
        return (left < right ? -1 : 1) * direction;
      });
    },
  },
  methods: {
    sortBy(key) {
      // Clicking the same column again reverses the sort.
      this.reverse = this.sortKey === key ? !this.reverse : false;
      this.sortKey = key;
    },
  },
}).mount('#app');
