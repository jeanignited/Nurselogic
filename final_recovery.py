import io
import re
import os

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Apply Mojibake Fix
c = c.replace('<%@ page pageEncoding="UTF-8" %>', '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>')

# 2. Get the new patient dashboard from update_patient_ui.py
with io.open('update_patient_ui.py', 'r', encoding='utf-8') as f:
    ui_script = f.read()
    # Extract the new_patient_dashboard string
    start_idx = ui_script.find("new_patient_dashboard = '''") + len("new_patient_dashboard = '''")
    end_idx = ui_script.find("'''", start_idx)
    new_patient_dashboard = ui_script[start_idx:end_idx]

# Add the 'Actualizado' date inside new_patient_dashboard
old_header = '<h3 class="mb-0 fw-bold" style="color: #10b981;">Mis Datos Cl&iacute;nicos</h3>'
new_header = '''<h3 class="mb-0 fw-bold" style="color: #10b981;">Mis Datos Cl&iacute;nicos</h3>
                    <span class="badge ms-auto py-2 px-3 fw-normal" style="background: rgba(16,185,129,0.1); color: #10b981; border: 1px solid rgba(16,185,129,0.2);">
                        <i class="bi bi-clock-history me-1"></i>Actualizado: <%= java.time.LocalDate.now().toString() %>
                    </span>'''
new_patient_dashboard = new_patient_dashboard.replace(old_header, new_header)

# Fix the stretches
new_patient_dashboard = new_patient_dashboard.replace('<div class="row g-4" id="formAgendar">', '<div class="row g-4 align-items-start" id="formAgendar">')
new_patient_dashboard = new_patient_dashboard.replace('<div class="form-section mt-0 h-100 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">\\n                        <div class="d-flex align-items-center mb-4">\\n                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(59,130,246,0.15);">\\n                                <i class="bi bi-calendar-plus text-primary fs-4"></i>', '<div class="form-section mt-0 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">\\n                        <div class="d-flex align-items-center mb-4">\\n                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(59,130,246,0.15);">\\n                                <i class="bi bi-calendar-plus text-primary fs-4"></i>')


# Replace the old VISTA DASHBOARD PACIENTE with our upgraded one
pattern = r'<!-- VISTA DASHBOARD PACIENTE -->.*?<% \} %>'
c = re.sub(pattern, new_patient_dashboard, c, flags=re.DOTALL)

# 3. Inject the 3 new views SAFELY right BEFORE the final <% } %> in dashboard_paciente
# Wait! new_patient_dashboard ends with <% } %>
# We should insert the new views right before that <% } %>
new_views = '''
        <!-- NUEVAS VISTAS DEL PACIENTE -->
        
        <!-- VISTA MIS CITAS PREVIAS -->
        <div id="citas_paciente" class="vista-activa d-none" style="position: relative; z-index: 1;">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-clock-history text-warning me-2"></i>Mis Citas Previas</h2>
            </div>
            
            <div class="card border-0 shadow-sm" style="background: var(--bg-panel); border-radius: 16px;">
                <div class="card-body p-4">
                    <% 
                       List<Map<String, String>> citasParaPac = (List<Map<String, String>>) request.getAttribute("listaCitas");
                       if(citasParaPac == null || citasParaPac.isEmpty()) { 
                    %>
                    <div class="text-center p-5">
                        <i class="bi bi-calendar-x text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                        <h3 class="fw-bold text-theme mt-4">No hay citas registradas</h3>
                    </div>
                    <% } else { %>
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover align-middle mb-0 text-theme">
                            <thead style="border-bottom: 2px solid rgba(0,0,0,0.05);">
                                <tr>
                                    <th class="py-3 text-secondary">Fecha</th>
                                    <th class="py-3 text-secondary">Hora</th>
                                    <th class="py-3 text-secondary">Especialidad</th>
                                    <th class="py-3 text-center text-secondary">Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <% for(Map<String,String> ct : citasParaPac) { %>
                                <tr style="border-bottom: 1px solid rgba(0,0,0,0.03);">
                                    <td class="py-3 fw-bold"><i class="bi bi-calendar-event me-2 text-primary"></i><%= ct.get("fecha") %></td>
                                    <td class="py-3"><i class="bi bi-clock me-2 text-secondary"></i><%= ct.get("hora") %></td>
                                    <td class="py-3 fw-medium"><%= ct.get("especialidad") %></td>
                                    <td class="py-3 text-center">
                                        <% if("ATENDIDO".equals(ct.get("estado"))) { %>
                                            <span class="badge bg-success px-3 py-2 rounded-pill"><i class="bi bi-check-circle me-1"></i>ATENDIDO</span>
                                        <% } else if("CANCELADO".equals(ct.get("estado"))) { %>
                                            <span class="badge bg-danger px-3 py-2 rounded-pill"><i class="bi bi-x-circle me-1"></i>CANCELADO</span>
                                        <% } else { %>
                                            <span class="badge bg-warning text-dark px-3 py-2 rounded-pill"><i class="bi bi-hourglass-split me-1"></i>PENDIENTE</span>
                                        <% } %>
                                    </td>
                                </tr>
                                <% } %>
                            </tbody>
                        </table>
                    </div>
                    <% } %>
                </div>
            </div>
        </div>

        <!-- VISTA RESULTADOS EXAMENES -->
        <div id="resultados_paciente" class="vista-activa d-none" style="position: relative; z-index: 1;">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-file-medical me-2" style="color: #c084fc;"></i>Resultados y Ex&aacute;menes</h2>
            </div>
            
            <div class="row g-4">
                <% 
                   boolean tieneResultados = false;
                   if(citasParaPac != null) {
                       for(Map<String,String> ct : citasParaPac) {
                           if(!"No registrado".equals(ct.get("diagnostico")) && ct.get("diagnostico") != null && !ct.get("diagnostico").trim().isEmpty()) {
                               tieneResultados = true;
                %>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-100 border-0 shadow-sm rounded-4" style="background: var(--bg-panel); transition: transform 0.2s;">
                        <div class="card-header border-0 bg-transparent pt-4 pb-0">
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="d-flex align-items-center">
                                    <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 40px; height: 40px; background: rgba(192, 132, 252, 0.1);">
                                        <i class="bi bi-clipboard2-pulse text-primary fs-5" style="color: #c084fc !important;"></i>
                                    </div>
                                    <span class="badge text-secondary border px-2 py-1"><%= ct.get("especialidad") %></span>
                                </div>
                                <span class="small text-secondary fw-bold"><i class="bi bi-calendar3 me-1"></i><%= ct.get("fecha") %></span>
                            </div>
                        </div>
                        <div class="card-body mt-2">
                            <h5 class="fw-bold text-theme mb-3">Diagn&oacute;stico Cl&iacute;nico</h5>
                            <p class="text-secondary" style="font-size: 0.95rem; line-height: 1.5;"><%= ct.get("diagnostico") %></p>
                        </div>
                    </div>
                </div>
                <% 
                           }
                       }
                   }
                   if(!tieneResultados) { 
                %>
                <div class="col-12">
                    <div class="card border-0 shadow-sm text-center p-5 rounded-4" style="background: var(--bg-panel);">
                        <i class="bi bi-droplet-half text-secondary mb-3" style="font-size: 4rem; opacity: 0.2;"></i>
                        <h4 class="fw-bold text-theme">Sin resultados de laboratorio</h4>
                    </div>
                </div>
                <% } %>
            </div>
        </div>

        <!-- VISTA MIS RECETAS -->
        <div id="recetas_paciente" class="vista-activa d-none" style="position: relative; z-index: 1;">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-capsule text-success me-2"></i>Mis Recetas M&eacute;dicas</h2>
            </div>
            
            <div class="row g-4">
                <% 
                   boolean tieneRecetas = false;
                   if(citasParaPac != null) {
                       for(Map<String,String> ct : citasParaPac) {
                           if(!"Ninguna".equals(ct.get("receta")) && ct.get("receta") != null && !ct.get("receta").trim().isEmpty()) {
                               tieneRecetas = true;
                %>
                <div class="col-md-6 col-lg-6">
                    <!-- Ticket Design -->
                    <div class="card border-0 shadow-sm h-100" style="background: var(--bg-panel); border-radius: 12px; border-left: 6px solid #10b981 !important;">
                        <div class="card-body p-4 d-flex flex-column">
                            <div class="d-flex justify-content-between align-items-start mb-3 border-bottom pb-3" style="border-color: rgba(0,0,0,0.05) !important;">
                                <div class="d-flex align-items-center">
                                    <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 48px; height: 48px; background: rgba(16, 185, 129, 0.1);">
                                        <i class="bi bi-capsule text-success fs-4"></i>
                                    </div>
                                    <div>
                                        <h5 class="fw-bolder m-0 text-theme">Prescripci&oacute;n M&eacute;dica</h5>
                                        <small class="text-secondary fw-semibold">Dra. / Dr. - <%= ct.get("especialidad") %></small>
                                    </div>
                                </div>
                                <div class="text-end">
                                    <span class="badge bg-light text-secondary border px-3 py-2 rounded-pill"><i class="bi bi-calendar-check me-1"></i><%= ct.get("fecha") %></span>
                                </div>
                            </div>
                            
                            <div class="flex-grow-1">
                                <div class="p-3 rounded-3" style="background: rgba(16,185,129,0.03);">
                                    <p class="mb-0 text-theme fw-medium" style="white-space: pre-line; line-height: 1.7; font-size: 0.95rem;">
                                        <i class="bi bi-prescription2 text-success me-2"></i><%= ct.get("receta") %>
                                    </p>
                                </div>
                            </div>
                            
                            <div class="d-flex justify-content-between align-items-center mt-4 pt-3 border-top" style="border-color: rgba(0,0,0,0.05) !important;">
                                <small class="text-secondary"><i class="bi bi-info-circle me-1"></i>Presente este ticket en farmacia</small>
                                <button class="btn btn-sm btn-success px-4 rounded-pill fw-bold shadow-sm" onclick="alert('Llevando a carrito de farmacia...')"><i class="bi bi-cart me-2"></i>Comprar</button>
                            </div>
                        </div>
                    </div>
                </div>
                <% 
                           }
                       }
                   }
                   if(!tieneRecetas) { 
                %>
                <div class="col-12">
                    <div class="card border-0 shadow-sm text-center p-5 rounded-4" style="background: var(--bg-panel);">
                        <i class="bi bi-prescription2 text-secondary mb-3" style="font-size: 4rem; opacity: 0.2;"></i>
                        <h4 class="fw-bold text-theme">Sin recetas activas</h4>
                    </div>
                </div>
                <% } %>
            </div>
        </div>

'''

# Find the LAST <% } %> in the file (which closes the if(!isPaciente) { ... } else { block)
last_index = c.rfind('<% } %>')
if last_index != -1:
    c = c[:last_index] + new_views + '\n        <% } %>'

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fully recovered dashboard.jsp successfully without 404 bugs!')
