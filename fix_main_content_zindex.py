import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add position:relative and z-index:1 to .main-content to ensure it is ABOVE the canvas
c = c.replace('.main-content { margin-left:var(--sidebar-w); transition:0.3s; padding:30px; }', '.main-content { margin-left:var(--sidebar-w); transition:0.3s; padding:30px; position: relative; z-index: 1; }')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed main-content z-index')
