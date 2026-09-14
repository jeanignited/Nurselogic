import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix Bienvenida card text
c = c.replace('<h1 class="display-5 fw-bold mb-3">', '<h1 class="display-5 fw-bold mb-3" style="color: white !important;">')
c = c.replace('<p class="fs-5 text-light opacity-75 mb-4" style="max-width: 800px; line-height: 1.6;">', '<p class="fs-5 opacity-75 mb-4" style="max-width: 800px; line-height: 1.6; color: rgba(255,255,255,0.9) !important;">')

# Fix Nota Importante background and text
c = c.replace('<div class="p-3 mt-3 mb-3 rounded bg-dark border border-secondary text-muted small">', '<div class="p-3 mt-3 mb-3 rounded border border-secondary small" style="background: var(--bg-panel); color: var(--text-color);">')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dashboard.jsp")
