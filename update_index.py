import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('z-index:0; pointer-events: none;', 'z-index:-1; pointer-events: none;')
c = c.replace('.main-content { margin-left:var(--sidebar-w); transition:0.3s; padding:30px; position: relative; z-index: 1; }', '.main-content { margin-left:var(--sidebar-w); transition:0.3s; padding:30px; position: relative; z-index: 10; }')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated index.jsp CSS logic")
