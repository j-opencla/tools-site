const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 9999;
const html = fs.readFileSync('D:/QClaw/workspace/index.html', 'utf8');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(html);
});

server.listen(PORT, '127.0.0.1', () => {
  console.log('Server running at http://127.0.0.1:' + PORT + '/');
});
