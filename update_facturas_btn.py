import io

with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_btn = '<a href="exportCsv?tipo=facturas" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</a>'
new_btn = '<button type="button" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV" onclick="exportarFacturasFechas()"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</button>'

c = c.replace(old_btn, new_btn)

with io.open('src/main/webapp/views/facturas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated facturas.jsp export button')
