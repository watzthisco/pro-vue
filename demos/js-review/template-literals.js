// Slides 272-273: template literals, tags and raw strings
// Run: node template-literals.js

const customer = { name: 'Penny' };
const order = { price: 4, product: 'parts', quantity: 6 };

const message = `Hi, ${customer.name}. Thank you for your order
of ${order.quantity} ${order.product} at $${order.price}.`;
console.log(message);

// A tag function receives the literal parts and the values separately
function tag(strings, ...values) {
  console.log('strings:', strings);
  console.log('raw[0]:', strings.raw[0]);
  console.log('values:', values);
}
tag`string text line 1 \n string text line 2 ${42}`;

console.log(String.raw`C:\new\folder`); // backslashes kept
