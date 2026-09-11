import io, re

# 1. Update personal.jsp to use data-bs-toggle
with io.open('src/main/webapp/views/personal.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()
c = c.replace('onclick="abrirModalNuevaEspecialidad()"', 'data-bs-toggle="modal" data-bs-target="#modalNuevaEspecialidad"')
with io.open('src/main/webapp/views/personal.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)

