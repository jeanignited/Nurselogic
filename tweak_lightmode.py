import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Soften light mode even more: lighter background, but more transparent panels so they don't look like solid white blocks
c = c.replace('--bg-main:#e2e8f0;', '--bg-main:#ebf0f6;')
c = c.replace('--bg-panel:rgba(255,255,255,0.85);', '--bg-panel:rgba(255,255,255,0.55);')
c = c.replace('--text-color:#0f172a;', '--text-color:#1e293b;') # Slightly softer text (slate-800 instead of 900)

# The user explicitly said the sidebar is "muy blanca". Let's give the sidebar a specific light mode tint.
sidebar_tint = '''html[data-bs-theme="light"] { --bg-main:#ebf0f6; --bg-panel:rgba(255,255,255,0.55); --text-color:#1e293b; --glass-border:1px solid rgba(0,0,0,0.08); }
        html[data-bs-theme="light"] .sidebar { background: linear-gradient(180deg, rgba(235,240,246,0.9) 0%, rgba(226,232,240,0.9) 100%); box-shadow: 2px 0 10px rgba(0,0,0,0.02); }'''

c = re.sub(r'html\[data-bs-theme="light"\] \{ --bg-main:#ebf0f6; --bg-panel:rgba\(255,255,255,0\.55\); --text-color:#1e293b; --glass-border:1px solid rgba\(0,0,0,0\.1\); \}', sidebar_tint, c)

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated light mode CSS')
