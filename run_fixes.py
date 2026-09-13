import io
import re

# 1. FIX PARTICLES IN INDEX.JSP
with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Remove canvas from its current position
idx_content = re.sub(r'<canvas id="globalParticles"[^>]*></canvas>', '', idx_content)

# Insert it at the top of main-content
replacement = '<div class="main-content" id="main-content">\n        <canvas id="globalParticles" style="position: absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events: none; opacity: 1;"></canvas>'
idx_content = idx_content.replace('<div class="main-content" id="main-content">', replacement)

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(idx_content)


# 2. FIX PARTICLES IN SCRIPTS.JSP (Remove constellation lines)
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    scr_content = f.read()

# Replace the animate loop to remove lines
new_animate = '''    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, width, height);
        
        let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light';
        let r = isLight ? 59 : 56;
        let g = isLight ? 130 : 189;
        let b = isLight ? 246 : 248;

        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];
            p.x += p.dx;
            p.y += p.dy;
            if (p.x < 0 || p.x > width) p.dx = -p.dx;
            if (p.y < 0 || p.y > height) p.dy = -p.dy;
            
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + p.alpha + ')';
            ctx.fill();
        }
    }'''

scr_content = re.sub(r'function animate\(\) \{.*?(?=\s+animate\(\);)', new_animate, scr_content, flags=re.DOTALL)
# Drop the particle count back to a reasonable number like 60 for non-connected dots
scr_content = scr_content.replace('i < 120; i++', 'i < 60; i++')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(scr_content)


# 3. FIX PATIENT DASHBOARD HTML
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    dash = f.read()

# Modify Mis Citas Previas
citas_html_new = '''        <!-- VISTA MIS CITAS PREVIAS -->
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
        </div>'''
dash = re.sub(r'<!-- VISTA MIS CITAS PREVIAS -->.*?</div>\s*</div>\s*</div>', citas_html_new, dash, flags=re.DOTALL)


# Modify Resultados
resultados_html_new = '''        <!-- VISTA RESULTADOS EXAMENES -->
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
        </div>'''
dash = re.sub(r'<!-- VISTA RESULTADOS EXAMENES -->.*?</div>\s*</div>\s*</div>', resultados_html_new, dash, flags=re.DOTALL)


# Modify Recetas
recetas_html_new = '''        <!-- VISTA MIS RECETAS -->
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
                                <!-- Asumiendo que el texto de receta viene completo, lo mostramos con estilo -->
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
        </div>'''
dash = re.sub(r'<!-- VISTA MIS RECETAS -->.*?</div>\s*</div>\s*</div>', recetas_html_new, dash, flags=re.DOTALL)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(dash)

print("Applied requested changes.")
