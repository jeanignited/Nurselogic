import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix Bienvenida card container
c = c.replace('<div class="p-5 mb-5 rounded-4 shadow-sm text-white position-relative overflow-hidden" style="background: linear-gradient(135deg, #1e293b, #0f172a); border-left: 5px solid #3b82f6;">',
              '<div class="p-5 mb-5 rounded-4 shadow-sm position-relative overflow-hidden" style="background: var(--bg-panel); border-left: 5px solid #3b82f6; border: var(--glass-border);">')

# Fix h1
c = c.replace('<h1 class="display-5 fw-bold mb-3" style="color: white !important;">',
              '<h1 class="display-5 fw-bold mb-3 text-theme">')

# Fix p
c = c.replace('<p class="fs-5 opacity-75 mb-4" style="max-width: 800px; line-height: 1.6; color: rgba(255,255,255,0.9) !important;">',
              '<p class="fs-5 opacity-75 mb-4 text-secondary" style="max-width: 800px; line-height: 1.6;">')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dashboard.jsp correctly")
