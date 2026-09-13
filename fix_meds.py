import io, re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(r'A\xf1adir', 'Añadir')
c = c.replace(r'f\xe1rmaco', 'fármaco')
c = c.replace(r'M\xfaltiple', 'Múltiple')

with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed JSP syntax in medicamentos.jsp")
