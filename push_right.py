import io

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    rep = f.read()

rep = rep.replace('class="form-check form-switch d-flex align-items-center me-3"', 'class="form-check form-switch d-flex align-items-center me-auto"')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(rep)
