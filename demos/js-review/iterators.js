// Slides 279-281: symbols, iterables and for...of
// Run: node iterators.js

const sym2 = Symbol('foo');
const sym3 = Symbol('foo');
console.log(sym2 === sym3); // false: every Symbol() is unique

// An iterable object with a generator method
const myIterable = {
  *[Symbol.iterator]() {
    yield 1;
    yield 2;
    yield 3;
  },
};
console.log([...myIterable]); // [1, 2, 3]

// An infinite iterator written by hand; the loop stops it with break
const fibonacci = {
  [Symbol.iterator]() {
    let pre = 0;
    let cur = 1;
    return {
      next() {
        [pre, cur] = [cur, pre + cur];
        return { done: false, value: cur };
      },
    };
  },
};

for (const n of fibonacci) {
  if (n > 1000) break;
  process.stdout.write(n + ' ');
}
console.log();

// for...of gives values; for...in gives keys
for (const v of ['a', 'b']) console.log('of:', v);
for (const k in ['a', 'b']) console.log('in:', k);
