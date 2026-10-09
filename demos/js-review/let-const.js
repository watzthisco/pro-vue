// Slides 263-264: const, let and var
// Run: node let-const.js

// var is function-scoped: the block reuses the outer variables
var a = 5;
var b = 10;
if (a === 5) {
  var a = 4;
  var b = 1;
}
console.log('var:', a, b); // 4 1

// let is block-scoped: the block gets its own variables
let c = 5;
let d = 10;
if (c === 5) {
  let c = 4;
  let d = 1;
}
console.log('let:', c, d); // 5 10

// const can't be reassigned, but the value isn't frozen
const user = { name: 'Ada' };
user.name = 'Grace'; // fine
console.log('const object changed:', user);
try {
  // eslint-disable-next-line no-const-assign
  user = {}; // TypeError
} catch (err) {
  console.log('reassigning const:', err.message);
}

// Temporal dead zone: let/const exist but can't be used before their declaration
try {
  console.log(early);
  let early = 1;
} catch (err) {
  console.log('TDZ:', err.message);
}
