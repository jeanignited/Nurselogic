# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Update patient sidebar links with colors and SweetAlert functionality
old_patient_sidebar = '''<% if(isPaciente) { %>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link active" onclick="cambiarVista('dashboard_paciente')"><i class="bi bi-house-heart"></i> Inicio</a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'});"><i class="bi bi-calendar-plus"></i> Agendar Cita</a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link"><i class="bi bi-clock-history"></i> Mis Citas Previas</a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link"><i class="bi bi-file-medical"></i> Resultados / Ex&aacute;menes</a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link"><i class="bi bi-capsule"></i> Mis Recetas</a>
    </li>'''

new_patient_sidebar = '''<% if(isPaciente) { %>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link active" onclick="cambiarVista('dashboard_paciente')"><i class="bi bi-house-heart text-primary"></i> <span class="texto-nav">Inicio</span></a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'});"><i class="bi bi-calendar-plus" style="color: #22d3ee;"></i> <span class="texto-nav">Agendar Cita</span></a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link" onclick="Swal.fire({icon: 'info', title: 'Mis Citas', text: 'No tienes citas previas registradas en el sistema.', confirmButtonColor: '#3b82f6'});"><i class="bi bi-clock-history text-warning"></i> <span class="texto-nav">Mis Citas Previas</span></a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link" onclick="Swal.fire({icon: 'info', title: 'Ex&aacute;menes', text: 'Tus resultados de laboratorio estar&aacute;n disponibles aqu&iacute; pr&oacute;ximamente.', confirmButtonColor: '#3b82f6'});"><i class="bi bi-file-medical" style="color: #c084fc;"></i> <span class="texto-nav">Resultados / Ex&aacute;menes</span></a>
    </li>
    <li class="nav-item mb-2">
        <a href="#" class="nav-link" onclick="Swal.fire({icon: 'info', title: 'Recetas', text: 'No tienes recetas m&eacute;dicas activas.', confirmButtonColor: '#3b82f6'});"><i class="bi bi-capsule text-success"></i> <span class="texto-nav">Mis Recetas</span></a>
    </li>'''

c = c.replace(old_patient_sidebar, new_patient_sidebar)

c = c.replace('<a href="#" class="btn btn-sm btn-primary w-100 fw-bold rounded-pill">Contactar Soporte</a>', '<a href="#" class="btn btn-sm btn-primary w-100 fw-bold rounded-pill" onclick="Swal.fire(\'Soporte T&eacute;cnico\', \'Puedes comunicarte al 1800-NURSELOGIC o escribir a soporte@nurselogic.com\', \'question\');">Contactar Soporte</a>')

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated patient sidebar colors and functionality')
