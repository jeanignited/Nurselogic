import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace any line containing // Cyan color with the correct code
lines = c.split('\n')
for i, line in enumerate(lines):
    if '// Cyan color' in line:
        lines[i] = "            ctx.fillStyle = 'rgba(56, 189, 248, ' + p.alpha + ')';"

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Fixed JS syntax error for particles robustly')
