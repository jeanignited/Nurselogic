import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<input type="date" name="fecha"', '<input type="date" id="citaFecha" name="fecha"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("document.getElementById('citaFechaHora');", "document.getElementById('citaFecha');")
c = c.replace("input.min = now.toISOString().slice(0, 16);", "input.min = now.toISOString().split('T')[0];")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
