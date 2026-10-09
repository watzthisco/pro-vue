// Slides 290-299: the four rules of `this`
// Run: node this-binding.js
// (This file is a CommonJS script, so plain functions run in sloppy mode.)

const author = {
  name: 'Chris',
  logName: function () {
    console.log('implicit:', this.name);
  },
};
author.logName(); // implicit: 'Chris'

// Implicit binding is lost when the method is passed around
const detached = author.logName;
detached(); // implicit: undefined (this is the global object)

// Explicit binding: call, apply, bind
function logFood(food1, food2) {
  console.log(`${this.name} likes ${food1} and ${food2}`);
}
logFood.call(author, 'tacos', 'soup');
logFood.apply(author, ['tacos', 'sushi']);
const bound = logFood.bind({ name: 'George' }, 'tacos');
bound('cherries');

// new binding
function City(state) {
  this.state = state;
}
console.log('new:', new City('CA').state);

// Default binding: the global object in sloppy mode...
globalThis.name = 'Harry';
function logName() {
  return this.name;
}
console.log('default (sloppy):', logName()); // 'Harry'

// ...and undefined in strict mode
function strictLogName() {
  'use strict';
  return this.name;
}
try {
  strictLogName();
} catch (err) {
  console.log('default (strict):', err.message);
}

// Arrow functions ignore all four rules and use the enclosing `this`
const timer = {
  name: 'timer',
  start() {
    setTimeout(() => console.log('arrow:', this.name), 0);
  },
};
timer.start();
