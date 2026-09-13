import io
import re

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Change the exportar button in agenda.jsp
# Current: <a href="exportCsv?tipo=citas" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</a>
new_btn = '''<button type="button" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV" onclick="exportarCitasFechas()"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</button>'''
c = re.sub(r'<a href="exportCsv\?tipo=citas".*?Exportar</a>', new_btn, c)

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated agenda.jsp export button')
