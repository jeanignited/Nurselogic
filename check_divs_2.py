import io
with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()
print(f'reportes.jsp divs: {c.count("<div")} / {c.count("</div")}')

with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='windows-1252') as f:
    c2 = f.read()
print(f'facturas.jsp divs: {c2.count("<div")} / {c2.count("</div")}')
