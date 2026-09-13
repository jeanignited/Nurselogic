import io
with io.open('src/main/webapp/views/estadisticas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('>Disponibilidad de Bodega</h5>', '>Disponibilidad de Bodega (Top 7)</h5>')
with io.open('src/main/webapp/views/estadisticas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated title in estadisticas.jsp')
