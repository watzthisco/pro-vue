// Slide 306: wrapping a callback API in a Promise by hand,
// and the built-in shortcut, util.promisify().
import fs from 'node:fs';
import { promisify } from 'node:util';

function readFileAsync(file, encoding) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, encoding, (err, data) => {
      if (err) return reject(err);
      resolve(data);
    });
  });
}

readFileAsync('text.txt', 'utf8').then(
  (data) => console.log('by hand:', data.trim()),
  (err) => console.error(err.message),
);

const readFilePromisified = promisify(fs.readFile);
readFilePromisified('text.txt', 'utf8').then((data) => console.log('promisify:', data.trim()));
