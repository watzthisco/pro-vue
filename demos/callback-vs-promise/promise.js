// Slide 305: the same thing with the promise-based fs API.
import { readFile } from 'node:fs/promises';

readFile('text.txt')
  .then((data) => console.log(data.toString()))
  .catch((err) => console.error('Could not read file:', err.message));

console.log('readFile returned a promise; this line runs first.');
