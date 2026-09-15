import io

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    rep = f.read()

rep = rep.replace('id="filtroNivelTI" class="form-select', 'id="filtroNivelTI" class="form-select w-auto')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(rep)
