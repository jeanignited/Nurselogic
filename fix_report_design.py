import io
import re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# Replace the card's main div
c = c.replace('<div class="card h-100 bg-dark" style="color: #fff !important; border: var(--glass-border); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">', 
              '<div class="card h-100 glass-card text-theme" style="overflow: hidden; border-radius: 12px;">')

# Replace the card header (optional: make it subtle)
c = c.replace('<div class="card-header border-0 d-flex justify-content-between align-items-center" style="background: rgba(255,255,255,0.05);">',
              '<div class="card-header border-0 d-flex justify-content-between align-items-center" style="border-bottom: var(--glass-border) !important; background: transparent;">')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
