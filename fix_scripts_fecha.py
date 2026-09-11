import io, re
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# find: document.getElementById('fichaFcSat').innerText = (fc > 0 ? fc + ' lpm' : '--') + ' / ' + (sat > 0 ? sat + '%' : '--');
c = c.replace(
    "document.getElementById('fichaFcSat').innerText = (fc > 0 ? fc + ' lpm' : '--') + ' / ' + (sat > 0 ? sat + '%' : '--');",
    "document.getElementById('fichaFcSat').innerText = (fc > 0 ? fc + ' lpm' : '--') + ' / ' + (sat > 0 ? sat + '%' : '--');\\n                        document.getElementById('fichaFechaActualizacion').innerHTML = '<i class=\"bi bi-calendar3 me-1\"></i> Fecha: ' + new Date().toLocaleDateString();"
)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
