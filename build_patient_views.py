import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the select scroll hack
c = re.sub(r'<style>.*?\.scrollable-select:focus.*?height: auto;.*?\}[\s\S]*?</style>\s*<select name="especialidad" class="form-select form-select-lg shadow-none scrollable-select"[^>]*>', '<select name="especialidad" class="form-select form-select-lg shadow-none" required style="border-radius: 10px; max-height: 250px;">', c)

# Fix the stretched row issue
# Find the formAgendar row and make it align-items-start so cards take natural height
c = c.replace('<div class="row g-4" id="formAgendar">', '<div class="row g-4 align-items-start" id="formAgendar">')
# Remove h-100 from the Agendar card
c = c.replace('<div class="form-section mt-0 h-100 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">\n                        <div class="d-flex align-items-center mb-4">\n                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(59,130,246,0.15);">\n                                <i class="bi bi-calendar-plus text-primary fs-4"></i>', '<div class="form-section mt-0 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">\n                        <div class="d-flex align-items-center mb-4">\n                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(59,130,246,0.15);">\n                                <i class="bi bi-calendar-plus text-primary fs-4"></i>')

# Add the 3 new views before <% } %>
new_views = '''
        <!-- NUEVAS VISTAS DEL PACIENTE -->
        
        <!-- VISTA MIS CITAS PREVIAS -->
        <div id="citas_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-clock-history text-warning me-2"></i>Mis Citas Previas</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-5 text-center" style="background: var(--bg-panel); border-radius: 16px;">
                <i class="bi bi-calendar-x text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                <h3 class="fw-bold text-theme mt-4">No hay citas registradas</h3>
                <p class="text-secondary fs-5 mb-4">A&uacute;n no tienes un historial de citas m&eacute;dicas en NurseLogic.</p>
                <button class="btn btn-primary px-4 py-2 rounded-pill shadow-sm" onclick="cambiarVista('dashboard_paciente'); setTimeout(()=>document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'}), 100);"><i class="bi bi-calendar-plus me-2"></i>Agendar tu primera cita</button>
            </div>
        </div>

        <!-- VISTA RESULTADOS EXAMENES -->
        <div id="resultados_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-file-medical me-2" style="color: #c084fc;"></i>Resultados y Ex&aacute;menes</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-5 text-center" style="background: var(--bg-panel); border-radius: 16px;">
                <i class="bi bi-droplet-half text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                <h3 class="fw-bold text-theme mt-4">Sin resultados de laboratorio</h3>
                <p class="text-secondary fs-5 mb-0">Cuando te realices ex&aacute;menes de sangre o imagenolog&iacute;a, los resultados aparecer&aacute;n aqu&iacute; autom&aacute;ticamente para que puedas descargarlos en PDF.</p>
            </div>
        </div>

        <!-- VISTA MIS RECETAS -->
        <div id="recetas_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-capsule text-success me-2"></i>Mis Recetas M&eacute;dicas</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-5 text-center" style="background: var(--bg-panel); border-radius: 16px;">
                <i class="bi bi-prescription2 text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                <h3 class="fw-bold text-theme mt-4">Recetario Vac&iacute;o</h3>
                <p class="text-secondary fs-5 mb-0">No tienes prescripciones o recetas activas en este momento. Si necesitas renovar medicamentos, agenda una consulta.</p>
            </div>
        </div>
'''

c = c.replace('<% } %>', new_views + '\n        <% } %>')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated dashboard with new views and fixes')
