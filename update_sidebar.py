import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the single Agendar Cita li for patients
pattern = r'<% if\(isPaciente\) \{ %>\s*<li class="nav-item"><a class="nav-link" onclick="cambiarVista\(\'dashboard_paciente\'\)">\s*<i class="bi bi-calendar-heart text-danger"></i><span class="texto-nav">Agendar Cita</span>\s*</a></li>\s*<% \} %>'

replacement = '''<% if(isPaciente) { %>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-inicio')">
                <i class="bi bi-calendar-heart text-danger"></i><span class="texto-nav">Agendar Cita</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-citas')">
                <i class="bi bi-clock-history text-warning"></i><span class="texto-nav">Mis Citas Previas</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-resultados')">
                <i class="bi bi-file-earmark-medical" style="color: var(--bs-purple, #6f42c1);"></i><span class="texto-nav">Resultados / Ex&aacute;menes</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-recetas')">
                <i class="bi bi-capsule text-success"></i><span class="texto-nav">Mis Recetas</span>
            </a></li>
            <% } %>'''

c = re.sub(pattern, replacement, c)

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("sidebar.jsp updated.")
