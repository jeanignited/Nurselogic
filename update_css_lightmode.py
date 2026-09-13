import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Soften light mode
c = c.replace('--bg-main:#f1f5f9;', '--bg-main:#e2e8f0;') # Make it slightly darker gray (Slate 200)
c = c.replace('--bg-panel:rgba(255,255,255,0.9);', '--bg-panel:rgba(255,255,255,0.75);') # Increase transparency slightly so background contrast helps, wait, if background is darker, panel being white with 0.9 is actually good contrast. Let's do 0.85.
c = c.replace('--bg-panel:rgba(255,255,255,0.75);', '--bg-panel:rgba(255,255,255,0.85);')

# Update .top-bar to block particles and stay on top
old_topbar = '.top-bar { display:flex; justify-content:space-between; margin-bottom:30px; border-bottom:var(--glass-border); padding-bottom:15px; }'
new_topbar = '.top-bar { display:flex; justify-content:space-between; margin-bottom:30px; border-bottom:var(--glass-border); padding: 15px 30px; margin: -30px -30px 30px -30px; background: var(--bg-main); position: sticky; top: 0; z-index: 100; transition: background-color 0.3s; }'
c = c.replace(old_topbar, new_topbar)

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated light mode colors and topbar CSS')
