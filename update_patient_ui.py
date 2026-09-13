import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add the UTF-8 directive at the very top (replacing the old one)
c = re.sub(r'<%@ page pageEncoding="UTF-8" %>', '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>', c)

# Prepare the new patient dashboard HTML
new_patient_dashboard = '''        <!-- VISTA DASHBOARD PACIENTE -->
        <div id="dashboard_paciente" class="vista-activa">
            
            <% if(request.getAttribute("mensaje") != null) { %>
                <div class="alert alert-success p-3 text-center mb-4 border-0 rounded-3 shadow-sm" style="background: rgba(16, 185, 129, 0.2); color: #34d399; backdrop-filter: blur(10px);"><i class="bi bi-check-circle me-2"></i><%= request.getAttribute("mensaje") %></div>
            <% } %>
            <% if(request.getAttribute("error") != null) { %>
                <div class="alert alert-danger p-3 text-center mb-4 border-0 rounded-3 shadow-sm" style="background: rgba(239, 68, 68, 0.2); color: #f87171; backdrop-filter: blur(10px);"><i class="bi bi-exclamation-octagon me-2"></i><%= request.getAttribute("error") %></div>
            <% } %>

            <!-- HERO SECTION / BANNER BIENVENIDA -->
            <div class="mb-5 p-5 rounded-4 shadow-sm position-relative overflow-hidden" style="background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(14,165,233,0.05) 100%); border: 1px solid rgba(59,130,246,0.2);">
                <div style="animation: fadeInDown 0.8s ease-out; position: relative; z-index: 2;">
                    <%
                        String nomPac = (String) session.getAttribute("nombres");
                        if(nomPac != null && !nomPac.trim().isEmpty() && !nomPac.contains("null")) {
                            nomPac = nomPac.trim().split(" ")[0];
                        } else {
                            nomPac = "Paciente";
                        }
                    %>
                    <h1 class="fw-bolder mb-3" style="font-size: 3rem; color: var(--text-color); letter-spacing: -1px;">
                        Bienvenido, <span style="color: #0ea5e9;"><%= nomPac %></span>
                    </h1>
                    <p class="fs-5 text-secondary" style="max-width: 800px; line-height: 1.6;">
                        Bienvenido a NurseLogic. Tu ecosistema de salud digital dise&ntilde;ado para darte control total sobre tu historial cl&iacute;nico, facilitar el agendamiento de tus citas y mantener una comunicaci&oacute;n directa con tus especialistas, todo en un solo lugar.
                    </p>
                    
                    <button class="btn btn-primary btn-lg mt-4 fw-bold shadow px-5 py-3 rounded-pill" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'});" style="background: linear-gradient(135deg, #0ea5e9, #2563eb); border: none;">
                        <i class="bi bi-calendar-plus-fill me-2"></i>Agendar Nueva Cita
                    </button>
                </div>
                <!-- Decorative Icon -->
                <i class="bi bi-heart-pulse text-primary position-absolute" style="font-size: 15rem; opacity: 0.05; right: -5%; top: -20%; transform: rotate(-15deg);"></i>
            </div>

            <% 
                Paciente miHC = (Paciente) request.getAttribute("miHistoriaClinica");
                if (miHC != null) {
            %>
            <!-- DATOS CLINICOS REESTRUCTURADOS -->
            <div class="form-section mt-0 mb-5 border-0 p-4" style="background: var(--bg-panel); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div class="d-flex align-items-center mb-4">
                    <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(16,185,129,0.15);">
                        <i class="bi bi-clipboard2-pulse-fill text-success fs-4"></i>
                    </div>
                    <h3 class="mb-0 fw-bold" style="color: #10b981;">Mis Datos Cl&iacute;nicos</h3>
                </div>
                
                <div class="row g-4">
                    <!-- Info General -->
                    <div class="col-md-6 col-lg-4">
                        <div class="p-3 rounded-3 h-100" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                            <div class="text-secondary small fw-semibold mb-1"><i class="bi bi-person-badge me-1"></i> Nombres Completos</div>
                            <div class="fs-5 fw-bold text-theme"><%= miHC.getNombres() %> <%= miHC.getApellidos() %></div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4">
                        <div class="p-3 rounded-3 h-100" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                            <div class="text-secondary small fw-semibold mb-1"><i class="bi bi-card-heading me-1"></i> C&eacute;dula</div>
                            <div class="fs-5 fw-bold text-theme"><%= miHC.getCedula() %></div>
                        </div>
                    </div>
                    <div class="col-md-12 col-lg-4">
                        <div class="p-3 rounded-3 h-100" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                            <div class="text-secondary small fw-semibold mb-1"><i class="bi bi-calendar-event me-1"></i> Fecha de Nacimiento</div>
                            <div class="fs-5 fw-bold text-theme"><%= (miHC.getFechaNacimiento() != null) ? miHC.getFechaNacimiento() : "Sin registrar" %></div>
                        </div>
                    </div>
                    
                    <!-- Vitals Cards -->
                    <div class="col-6 col-md-3">
                        <div class="p-4 rounded-4 text-center shadow-sm h-100" style="background: linear-gradient(145deg, var(--bg-panel), rgba(14,165,233,0.05)); border: 1px solid rgba(14,165,233,0.1);">
                            <i class="bi bi-rulers fs-2" style="color: #0ea5e9;"></i>
                            <div class="text-secondary mt-2 small fw-semibold">Estatura</div>
                            <div class="fs-4 fw-bolder text-theme mt-1"><%= miHC.getEstatura() %><span class="fs-6 text-secondary ms-1 fw-normal">m</span></div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="p-4 rounded-4 text-center shadow-sm h-100" style="background: linear-gradient(145deg, var(--bg-panel), rgba(245,158,11,0.05)); border: 1px solid rgba(245,158,11,0.1);">
                            <i class="bi bi-speedometer2 fs-2" style="color: #f59e0b;"></i>
                            <div class="text-secondary mt-2 small fw-semibold">Peso</div>
                            <div class="fs-4 fw-bolder text-theme mt-1"><%= miHC.getPeso() %><span class="fs-6 text-secondary ms-1 fw-normal">kg</span></div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="p-4 rounded-4 text-center shadow-sm h-100" style="background: linear-gradient(145deg, var(--bg-panel), rgba(239,68,68,0.05)); border: 1px solid rgba(239,68,68,0.1);">
                            <i class="bi bi-activity fs-2" style="color: #ef4444;"></i>
                            <div class="text-secondary mt-2 small fw-semibold">Presi&oacute;n</div>
                            <div class="fs-4 fw-bolder text-theme mt-1"><%= (miHC.getPresionArterial() != null && !miHC.getPresionArterial().trim().isEmpty()) ? miHC.getPresionArterial() : "--" %></div>
                        </div>
                    </div>
                    <div class="col-6 col-md-3">
                        <div class="p-4 rounded-4 text-center shadow-sm h-100" style="background: linear-gradient(145deg, var(--bg-panel), rgba(16,185,129,0.05)); border: 1px solid rgba(16,185,129,0.1);">
                            <i class="bi bi-thermometer-half fs-2" style="color: #10b981;"></i>
                            <div class="text-secondary mt-2 small fw-semibold">Temperatura</div>
                            <div class="fs-4 fw-bolder text-theme mt-1"><%= miHC.getTemperatura() %><span class="fs-6 text-secondary ms-1 fw-normal">&deg;C</span></div>
                        </div>
                    </div>
                </div>
            </div>
            <% } %>

            <div class="row g-4" id="formAgendar">
                <div class="col-lg-7">
                    <div class="form-section mt-0 h-100 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">
                        <div class="d-flex align-items-center mb-4">
                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(59,130,246,0.15);">
                                <i class="bi bi-calendar-plus text-primary fs-4"></i>
                            </div>
                            <h3 class="mb-0 fw-bold" style="color: #3b82f6;">Agendar Cita M&eacute;dica</h3>
                        </div>
                        <p class="text-secondary mb-4 fs-6">Selecciona la especialidad, fecha y hora para programar tu consulta con nuestros especialistas de confianza.</p>
                        
                        <form action="agendarCita" method="post" autocomplete="off" class="mt-auto">
                            <div class="mb-4">
                                <label class="form-label text-theme fw-bold"><i class="bi bi-hospital me-2 text-primary"></i>Especialidad Requerida</label>
                                <select name="especialidad" class="form-select form-select-lg shadow-none" required style="border-radius: 10px;">
                                    <option value="" disabled selected>Elige un &aacute;rea m&eacute;dica...</option>
                                    <%
                                        List<Map<String, String>> espMapPac = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");
                                        if(espMapPac != null && !espMapPac.isEmpty()) {
                                            for(Map<String, String> mEsp : espMapPac) {
                                                out.print("<option value='" + mEsp.get("id") + "'>" + mEsp.get("descripcion") + "</option>");
                                            }
                                        } else {
                                            out.print("<option value='1'>Medicina General</option>");
                                            out.print("<option value='2'>Odontolog&iacute;a</option>");
                                            out.print("<option value='3'>Pediatr&iacute;a</option>");
                                            out.print("<option value='4'>Ginecolog&iacute;a</option>");
                                        }
                                    %>
                                </select>
                            </div>

                            <div class="row g-4 mb-5">
                                <div class="col-md-6">
                                    <label class="form-label text-theme fw-bold"><i class="bi bi-calendar-event me-2 text-primary"></i>Fecha de la Cita</label>
                                    <input type="date" name="fecha" class="form-control form-control-lg shadow-none" min="<%= java.time.LocalDate.now().toString() %>" autocomplete="off" required style="border-radius: 10px;">
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label text-theme fw-bold"><i class="bi bi-clock me-2 text-primary"></i>Hora</label>
                                    <input type="time" name="hora" class="form-control form-control-lg shadow-none" required autocomplete="off" style="border-radius: 10px;">
                                </div>
                            </div>

                            <button type="submit" class="btn btn-primary w-100 py-3 fs-5 fw-bold shadow-sm" style="border-radius: 12px; background: linear-gradient(135deg, #3b82f6, #2563eb); border: none;">
                                <i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA
                            </button>
                        </form>
                    </div>
                </div>

                <div class="col-lg-5">
                    <div class="form-section mt-0 h-100 d-flex flex-column border-0 shadow-sm" style="background: var(--bg-panel);">
                        <div class="d-flex align-items-center mb-4">
                            <div class="rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 50px; height: 50px; background: rgba(16,185,129,0.15);">
                                <i class="bi bi-calculator text-success fs-4"></i>
                            </div>
                            <h3 class="mb-0 fw-bold" style="color: #10b981;">Calculadora de IMC</h3>
                        </div>
                        <p class="text-secondary mb-4 fs-6">Conoce tu &Iacute;ndice de Masa Corporal para un mejor seguimiento de tu salud.</p>
                        
                        <div class="mb-4 mt-2">
                            <label class="form-label text-theme fw-bold">Estatura (metros)</label>
                            <div class="input-group input-group-lg shadow-sm">
                                <span class="input-group-text bg-transparent text-secondary" style="border-right: none;"><i class="bi bi-rulers"></i></span>
                                <input type="text" id="estatura_pac" class="form-control" style="border-left: none; border-radius: 0 10px 10px 0;" maxlength="4" oninput="formatearEstatura_pac(this)" placeholder="Ej: 1.75" required autocomplete="off">
                            </div>
                        </div>
                        <div class="mb-5">
                            <label class="form-label text-theme fw-bold">Peso (kg)</label>
                            <div class="input-group input-group-lg shadow-sm">
                                <span class="input-group-text bg-transparent text-secondary" style="border-right: none;"><i class="bi bi-speedometer2"></i></span>
                                <input type="text" id="peso_pac" class="form-control" style="border-left: none; border-radius: 0 10px 10px 0;" maxlength="5" oninput="formatearPeso_pac(this)" placeholder="Ej: 70.5" required autocomplete="off">
                            </div>
                        </div>

                        <div class="imc-box flex-column align-items-center justify-content-center text-center p-4 mt-auto rounded-4" style="background: rgba(0,0,0,0.03); border: 1px dashed rgba(16,185,129,0.3);">
                            <div class="small text-secondary mb-2 fw-semibold text-uppercase tracking-wide">Tu Resultado IMC</div>
                            <span id="imcValor_pac" class="fw-bolder text-theme mb-2" style="font-size: 4rem; line-height: 1; color: #10b981 !important;">0.0</span>
                            <span id="imcEstado_pac" class="badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2 shadow-sm">Introduce tus datos</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <% } %>
'''

# Find the block and replace it
# The block starts at <!-- VISTA DASHBOARD PACIENTE --> and ends right before </div>\n    </div>\n</body>\n</html> (but inside the Java block? No, it ends at <% } %>)
pattern = r'<!-- VISTA DASHBOARD PACIENTE -->.*?<% \} %>'
c = re.sub(pattern, new_patient_dashboard, c, flags=re.DOTALL)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated patient dashboard UI')
