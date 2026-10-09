// Slides 277-278: array and object destructuring
// Run: node destructuring.js

const list = [1, 2, 3];
let [a, , b] = list;
console.log(a, b); // 1 3

[b, a] = [a, b]; // swap
console.log(a, b); // 3 1

const [first, ...rest] = list;
console.log(first, rest); // 1 [2, 3]

const { c, d, e } = { c: 1, d: 2, e: 3 };
console.log(c, d, e); // 1 2 3

const article = { title: 'Welcome', author: { username: 'ada' } };
const {
  title,
  author: { username },
} = article;
console.log(title, username);

const options = {};
const { count = 0 } = options;
console.log('count with default:', count);

// Renaming while destructuring
const { title: heading } = article;
console.log('renamed:', heading);
