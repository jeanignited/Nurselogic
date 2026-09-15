import io

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    rep = f.read()

# Make sure contenedorTicketsTI is row g-4 w-100
rep = rep.replace('<div class="row g-4" id="contenedorTicketsTI">', '<div class="row g-4 w-100" id="contenedorTicketsTI">')

# Make sure the top wrapper has the classes
rep = rep.replace('<div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">', '<div class="d-flex flex-wrap justify-content-between align-items-center gap-3 w-100 mb-4">')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(rep)
