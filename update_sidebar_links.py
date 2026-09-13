import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'Swal\.fire.*?Mis Citas.*?\}\);', "cambiarVista('citas_paciente')", c)
c = re.sub(r'Swal\.fire.*?Ex&aacute;menes.*?\}\);', "cambiarVista('resultados_paciente')", c)
c = re.sub(r'Swal\.fire.*?Recetas.*?\}\);', "cambiarVista('recetas_paciente')", c)

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated sidebar links safely')
