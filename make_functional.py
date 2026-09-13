import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace VISTA MIS CITAS PREVIAS
old_citas = '''        <!-- VISTA MIS CITAS PREVIAS -->
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
        </div>'''

new_citas = '''        <!-- VISTA MIS CITAS PREVIAS -->
        <div id="citas_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-clock-history text-warning me-2"></i>Mis Citas Previas</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-4" style="background: var(--bg-panel); border-radius: 16px;">
                <% 
                   List<Map<String, String>> citasParaPac = (List<Map<String, String>>) request.getAttribute("listaCitas");
                   if(citasParaPac == null || citasParaPac.isEmpty()) { 
                %>
                <div class="text-center p-5">
                    <i class="bi bi-calendar-x text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                    <h3 class="fw-bold text-theme mt-4">No hay citas registradas</h3>
                    <p class="text-secondary fs-5 mb-4">A&uacute;n no tienes un historial de citas m&eacute;dicas en NurseLogic.</p>
                    <button class="btn btn-primary px-4 py-2 rounded-pill shadow-sm" onclick="cambiarVista('dashboard_paciente'); setTimeout(()=>document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'}), 100);"><i class="bi bi-calendar-plus me-2"></i>Agendar tu primera cita</button>
                </div>
                <% } else { %>
                <div class="table-responsive">
                    <table class="table table-hover align-middle mb-0 text-theme">
                        <thead style="background: rgba(0,0,0,0.03);">
                            <tr>
                                <th class="border-0 rounded-start">Fecha</th>
                                <th class="border-0">Hora</th>
                                <th class="border-0">Especialidad</th>
                                <th class="border-0 text-center rounded-end">Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <% for(Map<String,String> ct : citasParaPac) { %>
                            <tr>
                                <td class="fw-bold"><i class="bi bi-calendar-event me-2 text-primary"></i><%= ct.get("fecha") %></td>
                                <td><i class="bi bi-clock me-2 text-secondary"></i><%= ct.get("hora") %></td>
                                <td><%= ct.get("especialidad") %></td>
                                <td class="text-center">
                                    <% if("ATENDIDO".equals(ct.get("estado"))) { %>
                                        <span class="badge bg-success px-3 py-2 rounded-pill shadow-sm"><i class="bi bi-check-circle me-1"></i><%= ct.get("estado") %></span>
                                    <% } else if("CANCELADO".equals(ct.get("estado"))) { %>
                                        <span class="badge bg-danger px-3 py-2 rounded-pill shadow-sm"><i class="bi bi-x-circle me-1"></i><%= ct.get("estado") %></span>
                                    <% } else { %>
                                        <span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm"><i class="bi bi-hourglass-split me-1"></i><%= ct.get("estado") %></span>
                                    <% } %>
                                </td>
                            </tr>
                            <% } %>
                        </tbody>
                    </table>
                </div>
                <% } %>
            </div>
        </div>'''
c = c.replace(old_citas, new_citas)

# Replace VISTA RESULTADOS EXAMENES
old_resultados = '''        <!-- VISTA RESULTADOS EXAMENES -->
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
        </div>'''

new_resultados = '''        <!-- VISTA RESULTADOS EXAMENES -->
        <div id="resultados_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-file-medical me-2" style="color: #c084fc;"></i>Diagn&oacute;sticos y Ex&aacute;menes</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-4" style="background: var(--bg-panel); border-radius: 16px;">
                <% 
                   boolean tieneResultados = false;
                   if(citasParaPac != null) {
                       for(Map<String,String> ct : citasParaPac) {
                           if(!"No registrado".equals(ct.get("diagnostico")) && ct.get("diagnostico") != null && !ct.get("diagnostico").trim().isEmpty()) {
                               tieneResultados = true;
                               break;
                           }
                       }
                   }
                   if(!tieneResultados) { 
                %>
                <div class="text-center p-5">
                    <i class="bi bi-droplet-half text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                    <h3 class="fw-bold text-theme mt-4">Sin resultados de laboratorio</h3>
                    <p class="text-secondary fs-5 mb-0">Tus diagn&oacute;sticos y resultados de ex&aacute;menes m&eacute;dicos aparecer&aacute;n aqu&iacute; luego de tus consultas.</p>
                </div>
                <% } else { %>
                <div class="row g-4">
                    <% for(Map<String,String> ct : citasParaPac) { 
                           if(!"No registrado".equals(ct.get("diagnostico")) && ct.get("diagnostico") != null && !ct.get("diagnostico").trim().isEmpty()) { %>
                    <div class="col-md-6">
                        <div class="p-4 rounded-4 shadow-sm h-100" style="background: rgba(192, 132, 252, 0.05); border: 1px solid rgba(192, 132, 252, 0.2);">
                            <div class="d-flex justify-content-between mb-3">
                                <span class="badge bg-primary rounded-pill"><i class="bi bi-calendar-event me-1"></i><%= ct.get("fecha") %></span>
                                <span class="badge text-secondary border"><%= ct.get("especialidad") %></span>
                            </div>
                            <h5 class="fw-bold text-theme mb-3"><i class="bi bi-clipboard2-pulse text-primary me-2"></i>Detalle del Diagn&oacute;stico</h5>
                            <p class="text-secondary mb-0" style="line-height: 1.6;"><%= ct.get("diagnostico") %></p>
                            <button class="btn btn-sm btn-outline-primary mt-3 rounded-pill shadow-sm" onclick="alert('Descarga de resultados en desarrollo.')"><i class="bi bi-download me-1"></i>Descargar PDF</button>
                        </div>
                    </div>
                    <%     }
                       } %>
                </div>
                <% } %>
            </div>
        </div>'''
c = c.replace(old_resultados, new_resultados)

# Replace VISTA MIS RECETAS
old_recetas = '''        <!-- VISTA MIS RECETAS -->
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
        </div>'''

new_recetas = '''        <!-- VISTA MIS RECETAS -->
        <div id="recetas_paciente" class="vista-activa d-none">
            <div class="mb-4 d-flex align-items-center">
                <button class="btn btn-outline-secondary rounded-circle me-3" onclick="cambiarVista('dashboard_paciente')" style="width: 45px; height: 45px;"><i class="bi bi-arrow-left"></i></button>
                <h2 class="fw-bold mb-0 text-theme"><i class="bi bi-capsule text-success me-2"></i>Mis Recetas M&eacute;dicas</h2>
            </div>
            
            <div class="form-section mt-0 border-0 shadow-sm p-4" style="background: var(--bg-panel); border-radius: 16px;">
                <% 
                   boolean tieneRecetas = false;
                   if(citasParaPac != null) {
                       for(Map<String,String> ct : citasParaPac) {
                           if(!"Ninguna".equals(ct.get("receta")) && ct.get("receta") != null && !ct.get("receta").trim().isEmpty()) {
                               tieneRecetas = true;
                               break;
                           }
                       }
                   }
                   if(!tieneRecetas) { 
                %>
                <div class="text-center p-5">
                    <i class="bi bi-prescription2 text-secondary" style="font-size: 5rem; opacity: 0.2;"></i>
                    <h3 class="fw-bold text-theme mt-4">Recetario Vac&iacute;o</h3>
                    <p class="text-secondary fs-5 mb-0">No tienes prescripciones o recetas m&eacute;dicas registradas en este momento.</p>
                </div>
                <% } else { %>
                <div class="row g-4">
                    <% for(Map<String,String> ct : citasParaPac) { 
                           if(!"Ninguna".equals(ct.get("receta")) && ct.get("receta") != null && !ct.get("receta").trim().isEmpty()) { %>
                    <div class="col-md-6">
                        <div class="p-4 rounded-4 shadow-sm h-100 position-relative" style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2);">
                            <div class="d-flex justify-content-between align-items-start mb-3">
                                <div>
                                    <span class="badge bg-success rounded-pill mb-2"><i class="bi bi-calendar-event me-1"></i><%= ct.get("fecha") %></span>
                                    <h5 class="fw-bold text-theme m-0"><i class="bi bi-heart-pulse text-success me-2"></i>Receta Emitida</h5>
                                </div>
                                <i class="bi bi-qr-code text-secondary opacity-50" style="font-size: 2rem;"></i>
                            </div>
                            <div class="p-3 bg-white rounded-3 shadow-sm my-3" style="border-left: 4px solid #10b981;">
                                <p class="text-dark mb-0 fw-semibold" style="white-space: pre-line;"><%= ct.get("receta") %></p>
                            </div>
                            <div class="d-flex justify-content-between align-items-center mt-3">
                                <span class="small text-secondary"><i class="bi bi-person-badge me-1"></i>Esp: <%= ct.get("especialidad") %></span>
                                <button class="btn btn-sm btn-success rounded-pill shadow-sm" onclick="alert('Funcionalidad de compra online en desarrollo.')"><i class="bi bi-cart-plus me-1"></i>Comprar en Farmacia</button>
                            </div>
                        </div>
                    </div>
                    <%     }
                       } %>
                </div>
                <% } %>
            </div>
        </div>'''
c = c.replace(old_recetas, new_recetas)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Replaced empty states with functional dynamic views')
