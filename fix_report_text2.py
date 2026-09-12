import io
with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

c = c.replace('<div class="card h-100 bg-dark" style="color: #fff !important;" style="border: var(--glass-border)', '<div class="card h-100 bg-dark" style="color: #fff !important; border: var(--glass-border)')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
