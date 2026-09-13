import io, re

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_badge = '<span class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-2 disabled" style="opacity: 1;"><i class="bi bi-clock me-2"></i>Turnos y Citas del D\u00EDa</span>'

c = c.replace('<span class="badge border border-secondary px-3 py-2" style="background-color: var(--bg-panel); color: var(--text-color);"><i class="bi bi-clock me-2"></i>Turnos y Citas del D\u00EDa</span>', new_badge)

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated badge to outline-secondary')
