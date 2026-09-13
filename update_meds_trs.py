# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('out.print("<tr>");', 'out.print("<tr data-id=\'" + m.get("id") + "\' data-nombre=\'" + m.get("nombre").replace("\'", "\\\\\'") + "\'>");')

with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated medicamentos.jsp TRs")
