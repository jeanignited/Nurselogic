import io

with io.open('src/main/webapp/views/estadisticas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('Especialidades Demandadas', 'Personal M\u00e9dico por Especialidad')

with io.open('src/main/webapp/views/estadisticas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
