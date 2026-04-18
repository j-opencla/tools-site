import re

with open(r'D:\QClaw\workspace\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For each tool panel script, we need to extract the function and expose it globally.
# Since innerHTML doesn't execute scripts, we have several options:
# 1. Use window.X = function to expose globally  
# 2. Use onclick attributes instead of script blocks
# 3. Use addEventListener after DOMContentLoaded

# Let's use approach: add the script text as global functions via eval at bottom of main script

# Extract all tool scripts
script_pattern = re.compile(r'<div class="tool-panel" id="panel-(\d+)">.*?<script>(.*?)</script></div>', re.DOTALL)
matches = script_pattern.findall(html)

all_script_texts = {}
for panel_id, script_content in matches:
    # Remove the auto-call at end (e.g. genPwd();) from each script
    script_clean = script_content.strip()
    # Extract just function definitions and setup (not auto-executed calls like genPwd())
    # Actually, we want to execute these too, but after they are defined
    # Let's collect them to add as a global script at bottom
    all_script_texts[panel_id] = script_content

print(f"Found {len(all_script_texts)} tool panel scripts")
for pid, sc in all_script_texts.items():
    print(f"  Panel {pid}: {len(sc)} chars")

# Now modify renderTools to execute scripts after innerHTML assignment
# Find the renderTools function and add script execution after grid.innerHTML=''
old_render_end = "    grid.appendChild(card);\n  });\n}"
new_render_end = """    grid.appendChild(card);
    // Execute scripts in this panel's content
    const scripts = card.querySelector('.tool-panel script');
    if (scripts) {
      try {
        const fn = new Function(scripts.textContent);
        fn.call(window);
      } catch(e) { console.error('Panel script error:', e); }
    }
  });
}"""

if old_render_end in html:
    html = html.replace(old_render_end, new_render_end)
    print("Successfully patched renderTools to execute panel scripts")
else:
    print("WARNING: Could not find exact renderTools end pattern")
    # Try to find it with flexible whitespace
    idx = html.find("grid.appendChild(card);")
    if idx != -1:
        print(f"Found grid.appendChild at {idx}")
        print(repr(html[idx:idx+100]))

# Also keep the fix after renderTools() call as backup
if 'querySelectorAll' not in html[html.find('renderTools()'):html.find('</script>', html.find('renderTools()'))]:
    print("Adding backup script execution after renderTools()")
else:
    print("Backup script already present")

with open(r'D:\QClaw\workspace\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("File saved")
