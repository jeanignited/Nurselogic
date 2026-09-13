import io
with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_badge = '<span class="badge bg-dark border border-secondary text-light px-3 py-2"><i class="bi bi-clock me-2"></i>Turnos y Citas del D\u00EDa</span>'
# Let's check if the raw text is exactly that (maybe different encoding in source)
