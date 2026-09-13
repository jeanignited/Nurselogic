# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('A\\xf1adir', 'A\u00F1adir')
c = c.replace('f\\xe1rmaco', 'f\u00E1rmaco')
c = c.replace('M\\xfaltiple', 'M\u00FAltiple')

with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed JSP syntax in medicamentos.jsp")
