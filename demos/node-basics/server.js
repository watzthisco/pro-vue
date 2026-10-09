// Slide 40 / Lab 08: a minimal HTTP server
// Run: node server.js, then open http://127.0.0.1:3000 (Ctrl+C to stop)
import http from 'node:http';

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  // This callback runs once per request
  console.log(`${req.method} ${req.url}`);
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
