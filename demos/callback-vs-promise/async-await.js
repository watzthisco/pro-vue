// Slide 307: async/await on top of promises.
import { readFile } from 'node:fs/promises';

async function readText(file) {
  const data = await readFile(file, 'utf8'); // pauses here until the promise settles
  return data.trim();
}

try {
  // Top-level await works in ES modules
  const text = await readText('text.txt');
  console.log(text);

  // Run several reads in parallel
  const [a, b] = await Promise.all([readText('text.txt'), readText('text.txt')]);
  console.log('read twice in parallel:', a.length + b.length, 'characters');

  // Rejections become exceptions you can catch
  await readText('missing.txt');
} catch (err) {
  console.error('Caught:', err.code, err.message);
}
