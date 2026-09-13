import io, re

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_badge = '<span class="badge border border-secondary px-3 py-2" style="background-color: var(--bg-panel); color: var(--text-color);"><i class="bi bi-clock me-2"></i>Turnos y Citas del D\u00EDa</span>'

# Replace using regex
c = re.sub(r'<span class="badge bg-dark border border-secondary text-light px-3 py-2"><i class="bi bi-clock me-2"></i>Turnos y Citas del D[^<]+</span>', new_badge, c)

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated badge in agenda.jsp')
