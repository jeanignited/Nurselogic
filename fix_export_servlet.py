import io

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('d.getMedicamentoNombre()', 'd.getMedicamento().getNombre()')

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed getMedicamentoNombre to getMedicamento().getNombre() in ExportServlet.java')
