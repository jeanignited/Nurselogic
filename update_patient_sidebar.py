import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# The patient block in sidebar.jsp
# <% if(isPaciente) { %>
#     <li class="nav-item mb-2">
#         <a href="#" class="nav-link active" onclick="cambiarVista('dashboard_paciente')"><i class="bi bi-calendar2-heart"></i> Agendar Cita</a>
#     </li>
# <% } %>

new_patient_sidebar = '''<% if(isPaciente) { %>
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
    </li>
    
    <div class="mt-auto px-3 pb-3">
        <div class="p-3 rounded-3" style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2);">
            <div class="d-flex align-items-center mb-2">
                <i class="bi bi-info-circle-fill text-primary me-2"></i>
                <strong class="text-theme fs-6">Centro de Ayuda</strong>
            </div>
            <p class="small text-secondary mb-2" style="font-size: 0.8rem;">Tienes dudas con tu cita o historial? Contctanos.</p>
            <a href="#" class="btn btn-sm btn-primary w-100 fw-bold rounded-pill">Contactar Soporte</a>
        </div>
        <div class="p-3 rounded-3 mt-3 text-center" style="background: rgba(239,68,68,0.1); border: 1px dashed rgba(239,68,68,0.3);">
            <i class="bi bi-telephone-fill text-danger mb-1 fs-5 d-block"></i>
            <strong class="text-danger d-block">Emergencias</strong>
            <h4 class="text-danger fw-bolder mb-0">911</h4>
        </div>
    </div>
<% } %>'''

c = re.sub(r'<% if\(isPaciente\) \{ %>.*?<% \} %>', new_patient_sidebar, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated patient sidebar')
