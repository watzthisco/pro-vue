const PEOPLE = [
  { name: 'Ping', age: 20 },
  { name: 'Amir', age: 24 },
  { name: 'Shabnum', age: 30 },
  { name: 'Mark', age: 40 },
];

const { createApp, ref, computed } = Vue;

createApp({
  setup() {
    const searchDetails = ref('');
    const sortKey = ref('name');
    const reverse = ref(false);
    const people = ref(PEOPLE);

    // A computed property is cached: it only re-runs when one of the
    // reactive values it reads actually changes.
    const filterIt = computed(() => {
      const term = searchDetails.value.trim().toLowerCase();

      const matches = people.value.filter(
        (person) =>
          person.name.toLowerCase().includes(term) ||
          String(person.age).includes(term),
      );

      const direction = reverse.value ? -1 : 1;

      return [...matches].sort((a, b) => {
        const left = a[sortKey.value];
        const right = b[sortKey.value];

        if (left === right) return 0;
        return (left < right ? -1 : 1) * direction;
      });
    });

    function sortBy(key) {
      // Clicking the same column again reverses the sort.
      reverse.value = sortKey.value === key ? !reverse.value : false;
      sortKey.value = key;
    }

    return { searchDetails, filterIt, sortBy };
  },
}).mount('#app');
