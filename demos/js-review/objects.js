// Slides 274-276: property shorthand, computed names, method shorthand
// Run: node objects.js

const x = 1;
const y = 2;
console.log({ x: x, y: y }, { x, y }); // same thing

let orderNum = 41;
function getOrderNum() {
  return ++orderNum;
}
const obj = {
  customer: 'Nigel',
  ['order' + getOrderNum()]: 10,
};
console.log(obj); // { customer: 'Nigel', order42: 10 }

const field = 'email';
console.log({ [field]: 'ada@example.com' });

const counter = {
  count: 0,
  increment() {
    this.count++;
    return this.count;
  },
};
console.log(counter.increment(), counter.increment());
