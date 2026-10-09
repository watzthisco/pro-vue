// Slides 269-270: default and rest parameters
// Run: node parameters.js

function withDefaults(x, y = 0, z = 13) {
  return x + y + z;
}
console.log(withDefaults(4)); // 17
console.log(withDefaults(4, 1)); // 18
console.log(withDefaults(4, undefined, 1)); // 5: undefined triggers the default
console.log(withDefaults(4, null, 1)); // 5: null does NOT (null + 4 + 1)

function myFunc(x, y, ...a) {
  console.log('a is', a, 'Array?', Array.isArray(a));
  return (x + y) * a.length;
}
console.log(myFunc(1, 2, 'hello', true, 7)); // 9
