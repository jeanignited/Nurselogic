import io

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_paciente_block = '''            <% if(isPaciente) { %>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-inicio')">
                <i class="bi bi-calendar-heart text-danger"></i><span class="texto-nav">Agendar Cita</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-citas')">
                <i class="bi bi-clock-history text-warning"></i><span class="texto-nav">Mis Citas</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-resultados')">
                <i class="bi bi-file-earmark-medical" style="color: var(--bs-purple, #6f42c1);"></i><span class="texto-nav">Resultados / Ex&aacute;menes</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-recetas')">
                <i class="bi bi-capsule text-success"></i><span class="texto-nav">Mis Recetas</span>
            </a></li>
            <% } %>'''

new_paciente_block = '''            <% if(isPaciente) { %>
            <li class="nav-item"><a class="nav-link active btn-inicio" href="#" onclick="switchPacienteTab('vista-inicio', this)">
                <i class="bi bi-house text-primary"></i><span class="texto-nav">Inicio</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-inicio', document.querySelector('.btn-inicio')); setTimeout(() => document.getElementById('contenedor-agendar').scrollIntoView({behavior: 'smooth'}), 50);">
                <i class="bi bi-calendar-heart text-danger"></i><span class="texto-nav">Agendar Cita</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-citas', this)">
                <i class="bi bi-clock-history text-warning"></i><span class="texto-nav">Mis Citas</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-resultados', this)">
                <i class="bi bi-file-earmark-medical" style="color: var(--bs-purple, #6f42c1);"></i><span class="texto-nav">Resultados / Ex&aacute;menes</span>
            </a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="switchPacienteTab('vista-recetas', this)">
                <i class="bi bi-capsule text-success"></i><span class="texto-nav">Mis Recetas</span>
            </a></li>
            <% } %>'''

c = c.replace(old_paciente_block, new_paciente_block)

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated sidebar.jsp")
