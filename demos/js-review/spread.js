// Slide 271: spread
// Run: node spread.js

function myFunc(x, y, ...rest) {
  return `${x}, ${y}, and ${rest.length} more`;
}

const params = ['hello', true, 7];
const other = [1, 2, ...params];
console.log(other); // [1, 2, 'hello', true, 7]

console.log(myFunc(1, 2, ...params)); // same as myFunc(1, 2, 'hello', true, 7)

const chars = [...'foo'];
console.log(chars); // ['f', 'o', 'o']

// Object spread: a shallow copy with one property overridden
const user = { name: 'Chris', city: 'Astoria' };
const copy = { ...user, name: 'Ada' };
console.log(user, copy);
