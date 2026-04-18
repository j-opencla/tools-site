const fs = require('fs');
let html = fs.readFileSync('D:\\QClaw\\workspace\\index.html', 'utf8');

// Check the current state of renderTools
const renderIdx = html.indexOf('function renderTools');
const renderEndIdx = html.indexOf('grid.appendChild(card);', renderIdx);
console.log('renderTools found at:', renderIdx);
console.log('grid.appendChild found at:', renderEndIdx);
const renderChunk = html.substring(renderEndIdx - 50, renderEndIdx + 100);
console.log('Around appendChild:', JSON.stringify(renderChunk));

// Check if we already have the fix
const hasFix = html.includes('new Function(scripts.textContent)');
console.log('Has fix already:', hasFix);

// Check renderTools() call context
const rtCall = html.indexOf('renderTools();');
console.log('renderTools() call at:', rtCall);
console.log('After call:', JSON.stringify(html.substring(rtCall, rtCall+500)));
