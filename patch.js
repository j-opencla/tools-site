const fs = require('fs');
let h = fs.readFileSync('D:/QClaw/workspace/index.html', 'utf8');

const old = `renderTools();
    // 修复: innerHTML 插入的 script 标签不会自动执行，强制重新加载
    document.querySelectorAll('.tool-panel script').forEach(old => {
      const s = document.createElement('script');
      [...old.attributes].forEach(a => s.setAttribute(a.name, a.value));
      s.textContent = old.textContent;
      old.parentNode.replaceChild(s, old);
    });`;

const fresh = `renderTools();
    (function(){
      document.querySelectorAll(".tool-panel script").forEach(function(s){
        try{ (new Function(s.textContent)).call(window); }catch(e){console.error(e);}
      });
    })();`;

if (h.includes(old)) {
  h = h.replace(old, fresh);
  fs.writeFileSync('D:/QClaw/workspace/index.html', h, 'utf8');
  console.log('Patched successfully!');
} else {
  console.log('Pattern not found');
  const idx = h.indexOf('renderTools()');
  console.log(JSON.stringify(h.substring(idx, idx + 600)));
}
