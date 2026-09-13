import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<i class="bi bi-clock-history text-warning"></i><span class="texto-nav">Mis Citas Previas</span>', '<i class="bi bi-clock-history text-warning"></i><span class="texto-nav">Mis Citas</span>')

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Sidebar text changed.")
