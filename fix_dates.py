import io, re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('id="recetaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento"', 'id="recetaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>"')

c = c.replace('id="camaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento"', 'id="camaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>"')

c = c.replace('id="citaFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento"', 'id="citaFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added max attribute to modals.jsp")
