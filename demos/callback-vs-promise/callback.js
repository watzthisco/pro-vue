// Slide 305: Node's original callback style.
// The callback's first argument is the error (or null).
import fs from 'node:fs';

fs.readFile('text.txt', (err, file) => {
  if (err) console.error('Could not read file:', err.message);
  else console.log(file.toString());
});

console.log('readFile was called; this line runs first, because readFile is non-blocking.');
