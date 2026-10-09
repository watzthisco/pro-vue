// Slides 266-268: arrow functions
// Run: node arrow-functions.js

const increment = function (v) {
  return v + 1;
};
const incrementArrow = (v) => v + 1; // concise body: value is returned
const buggy = (v) => {
  v + 1; // block body without return: returns undefined!
};
const fixed = (v) => {
  return v + 1;
};
console.log(increment(1), incrementArrow(1), buggy(1), fixed(1)); // 2 2 undefined 2

// Returning an object literal needs parentheses
const makeState = () => ({ count: 0 });
console.log(makeState());

// Arrow functions use the surrounding `this`
const collector = {
  nums: [5, 7, 10, 15],
  fives: [],
  collect() {
    this.nums.forEach((v) => {
      if (v % 5 === 0) this.fives.push(v); // `this` is collector
    });
    return this.fives;
  },
};
console.log(collector.collect()); // [5, 10, 15]
