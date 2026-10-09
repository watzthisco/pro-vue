// Slide 282: generator functions
// Run: node generators.js

function* idMaker() {
  let index = 0;
  while (true) {
    yield index++;
  }
}

const gen = idMaker();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
console.log(gen.next()); // { value: 2, done: false }

// A finite generator works with spread and for...of
function* range(start, end) {
  for (let i = start; i < end; i++) yield i;
}
console.log([...range(1, 6)]); // [1, 2, 3, 4, 5]
