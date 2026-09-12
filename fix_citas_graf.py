import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('"CANCELADA".equalsIgnoreCase(est)', 'est != null && est.toUpperCase().startsWith("CANCEL")')
c = c.replace('"ATENDIDO".equalsIgnoreCase(est)', 'est != null && (est.toUpperCase().startsWith("ATEND") || est.toUpperCase().startsWith("DESPACH"))')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
