# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Ver PDF button
old_pdf = '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-file-earmark-pdf me-2"></i>Ver PDF</button>'
new_pdf = '<button class="btn btn-sm btn-outline-primary" onclick="simularAperturaDocumento(\'Resultado/Examen\')"><i class="bi bi-file-earmark-pdf me-2"></i>Ver PDF</button>'
c = c.replace(old_pdf, new_pdf)

# Replace Ver Receta button
old_receta = '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-capsule me-2"></i>Ver Receta</button>'
new_receta = '<button class="btn btn-sm btn-outline-primary" onclick="simularAperturaDocumento(\'Receta M\u00E9dica\')"><i class="bi bi-capsule me-2"></i>Ver Receta</button>'
c = c.replace(old_receta, new_receta)

# Inject simularAperturaDocumento function
old_script_start = 'document.addEventListener("DOMContentLoaded", initPacienteParticles);'
new_script_start = '''document.addEventListener("DOMContentLoaded", initPacienteParticles);

window.simularAperturaDocumento = function(tipo) {
    alert("Generando " + tipo + " en formato PDF... El documento se abrir\u00E1 en una nueva pesta\u00F1a.");
};'''
c = c.replace(old_script_start, new_script_start)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated dashboard.jsp")
