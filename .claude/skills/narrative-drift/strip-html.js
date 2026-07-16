// แปลง 10-K HTML (inline XBRL) เป็น plain text อ่านง่าย ตัด tag/script/style ออก
// Usage: node strip-html.js <input.htm> <output.txt>
const fs = require('fs');
const [, , input, output] = process.argv;

let html = fs.readFileSync(input, 'utf8');
html = html.replace(/<script[\s\S]*?<\/script>/gi, '');
html = html.replace(/<style[\s\S]*?<\/style>/gi, '');
html = html.replace(/<(tr|\/tr|p|\/p|div|\/div|br)[^>]*>/gi, '\n');
html = html.replace(/<[^>]+>/g, ' ');
html = html
  .replace(/&nbsp;/g, ' ')
  .replace(/&amp;/g, '&')
  .replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>')
  .replace(/&#\d+;/g, ' ')
  .replace(/&#x[0-9a-f]+;/gi, ' ');
html = html.replace(/[ \t]+/g, ' ').replace(/\n{3,}/g, '\n\n');

fs.writeFileSync(output, html);
console.error(`Wrote ${output} (${html.length} chars)`);
