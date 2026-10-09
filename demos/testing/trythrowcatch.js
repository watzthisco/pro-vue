// Slide 228: an assertion written by hand with try/throw/catch.
// Run: node trythrowcatch.js
// It FAILS on purpose (red): hello() is missing the "!".
// Fix hello(), run it again, and it passes (green).

function hello(name) {
  return 'Hello, ' + name;
}

const result = hello('World');
const expected = 'Hello, World!';

try {
  if (result !== expected) {
    throw new Error(`Expected ${expected} but got ${result}`);
  }
  console.log('PASS');
} catch (err) {
  console.log('FAIL:', err.message);
  process.exitCode = 1;
}
