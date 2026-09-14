import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function abrirModalAtenderCita.*?\}', c, re.DOTALL)
if m:
    old_code = m.group(0)
    new_code = old_code.replace('''    document.getElementById("atenderIdCita").value = idCita;
    document.getElementById("atenderPacNombre").value = pacienteNombre;

    var pacienteLabel = document.getElementById("atenderCitaPaciente");
    if (pacienteLabel) {
        pacienteLabel.innerText = pacienteNombre;
    }

    var form = document.getElementById("formAtenderCita");
    if (form) {
        form.reset();
    }''', '''    var form = document.getElementById("formAtenderCita");
    if (form) {
        form.reset();
    }

    document.getElementById("atenderIdCita").value = idCita;
    document.getElementById("atenderPacNombre").value = pacienteNombre;

    var pacienteLabel = document.getElementById("atenderCitaPaciente");
    if (pacienteLabel) {
        pacienteLabel.innerText = pacienteNombre;
    }''')
    c = c.replace(old_code, new_code)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed order of reset")
else:
    print("Not found")
