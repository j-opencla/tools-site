import re

html = open(r'D:\QClaw\workspace\index.html', 'r', encoding='utf-8').read()

old_section = """renderTools();
    // 修复: innerHTML 插入的 script 标签不会自动执行，强制重新加载
    document.querySelectorAll('.tool-panel script').forEach(old => {
      const s = document.createElement('script');
      [...old.attributes].forEach(a => s.setAttribute(a.name, a.value));
      s.textContent = old.textContent;
      old.parentNode.replaceChild(s, old);
    });"""

new_section = """renderTools();
    (function() {
      var scripts = document.querySelectorAll('.tool-panel script');
      scripts.forEach(function(old) {
        try { (new Function(old.textContent)).call(window); } catch(e) { console.error(e); }
      });
    })();"""

if old_section in html:
    html = html.replace(old_section, new_section)
    print('Patched successfully!')
else:
    print('Not found')
    idx = html.find('renderTools()')
    print('renderTools() at:', idx)
    print(repr(html[idx:idx+400]))

open(r'D:\QClaw\workspace\index.html', 'w', encoding='utf-8').write(html)
print('Done')
