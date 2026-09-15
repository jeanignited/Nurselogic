import io
import re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    rep = f.read()

rep = rep.replace('<div class="d-flex gap-2">', '<div class="d-flex flex-wrap align-items-center gap-3 w-100">')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(rep)
