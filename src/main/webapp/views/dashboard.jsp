<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.List,java.util.Map" %>
<%@ page import="com.nurselogic.model.*" %>
<%
    boolean isAdmin        = Boolean.TRUE.equals(request.getAttribute("isAdmin"));
    boolean isPaciente     = Boolean.TRUE.equals(request.getAttribute("isPaciente"));
    boolean isFarmaceutico = Boolean.TRUE.equals(request.getAttribute("isFarmaceutico"));
    boolean permPac        = Boolean.TRUE.equals(request.getAttribute("permPac"));
    boolean permMed        = Boolean.TRUE.equals(request.getAttribute("permMed"));
    boolean permCat        = Boolean.TRUE.equals(request.getAttribute("permCat"));
    boolean canSellStock   = Boolean.TRUE.equals(request.getAttribute("canSellStock"));
    boolean canManageStock = Boolean.TRUE.equals(request.getAttribute("canManageStock"));
    boolean permCitas      = Boolean.TRUE.equals(request.getAttribute("permCitas"));
    boolean permUsuarios   = Boolean.TRUE.equals(request.getAttribute("permUsuarios"));
    String correoLogueado  = (String) request.getAttribute("correoLogueado");
    String rolUsuario      = (String) request.getAttribute("rolUsuario");
%>        <% if(!isPaciente) { %>

        <!-- VISTA DASHBOARD MEDICO/ADMIN -->

                <div id="dashboard" class="vista-activa position-relative" style="min-height: 80vh; overflow: visible; border-radius: 12px; padding: 20px;">
            <div class="mb-5 text-center" style="animation: fadeInDown 0.8s ease-out;">
                <%
                    String nombreBienvenida = (String) session.getAttribute("nombres");
                    if(nombreBienvenida != null && !nombreBienvenida.trim().isEmpty() && !nombreBienvenida.contains("null")) {
                        nombreBienvenida = nombreBienvenida.trim();
                    } else {
                        nombreBienvenida = "Usuario";
                    }
                %>
                <h2 class="fw-bold text-white mb-2" style="font-size: 2.5rem; letter-spacing: -0.5px;">Bienvenido, <span style="color: #38bdf8;"><%= nombreBienvenida %></span></h2>
                <p class="text-secondary fs-5">Este es el resumen de actividad de tu centro m&eacute;dico hoy.</p>
            </div>


            <div class="row g-4 mb-5">

                <% if(permPac) { %>

                <div class="col-md-4">

                    <div class="kpi-card h-100" onclick="cambiarVista('pacientes')">

                        <div class="kpi-title"><i class="bi bi-person-heart me-2 text-primary"></i>Pacientes Registrados</div>

                        <div class="kpi-number"><%= request.getAttribute("totalPacientes") != null ? request.getAttribute("totalPacientes") : "0" %></div>

                    </div>

                </div>

                <% } %>

                <% if(permMed) { %>

                <div class="col-md-4">

                    <div class="kpi-card h-100" onclick="cambiarVista('medicamentos')">

                        <div class="kpi-title"><i class="bi bi-capsule me-2" style="color: #10b981;"></i>Medicamentos en Stock</div>

                        <div class="kpi-number"><%= request.getAttribute("totalMeds") != null ? request.getAttribute("totalMeds") : "0" %></div>

                    </div>

                </div>

                <% } %>

                <% if(permUsuarios) { %>

                <div class="col-md-4">

                    <div class="kpi-card h-100" onclick="cambiarVista('personal')">

                        <div class="kpi-title"><i class="bi bi-people-fill me-2" style="color: #f59e0b;"></i>Personal M&eacute;dico</div>

                        <div class="kpi-number"><%= request.getAttribute("totalUsers") != null ? request.getAttribute("totalUsers") : "0" %></div>

                    </div>

                </div>

                <% } %>

            </div>

            

            <div class="d-flex justify-content-end gap-3 mb-4">

                <% if(permPac) { %>

                <button type="button" class="btn btn-info btn-lg text-dark fw-bold shadow-sm" style="background: linear-gradient(135deg, #38bdf8, #0ea5e9); border: none;" onclick="document.getElementById('formAdmision').classList.toggle('d-none'); if(!document.getElementById('formAdmision').classList.contains('d-none')) { document.getElementById('formAdmision').scrollIntoView({behavior: 'smooth'}); }">

                    <i class="bi bi-person-plus-fill me-2"></i>Nueva Admisión

                </button>

                <% } %>

                <button type="button" class="btn btn-info btn-lg text-dark fw-bold shadow-sm" style="background: linear-gradient(135deg, #38bdf8, #0ea5e9); border: none;" onclick="cambiarVista('agenda')">

                    <i class="bi bi-calendar2-week-fill me-2"></i>Ver Agenda M&eacute;dica

                </button>

            </div>



            <div class="form-section d-none" id="formAdmision">

                <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-file-earmark-medical me-2"></i>Nueva Admisión y Triage</h4>

                <form action="registroPaciente" method="post" id="formRegistroPaciente" autocomplete="off">

                    <div class="row g-4 mb-4">

                        <div class="col-md-3"><label class="form-label small text-secondary fw-semibold">Nombres</label><input type="text" name="nombres" id="nombres" class="form-control" required autocomplete="off"></div>

                        <div class="col-md-3"><label class="form-label small text-secondary fw-semibold">Apellidos</label><input type="text" name="apellidos" id="apellidos" class="form-control" required autocomplete="off"></div>

                        <div class="col-md-2"><label class="form-label small text-secondary fw-semibold">Cédula</label><input type="text" name="cedula" id="cedulaBusqueda" class="form-control" pattern="\d{10}" maxlength="10" title="Debe contener exactamente 10 dígitos" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>

                        <div class="col-md-2"><label class="form-label small text-secondary fw-semibold">Fecha Nacimiento <span id="edadBadge" class="badge bg-info ms-1 d-none" style="font-size: 0.75rem;">0 años</span></label><input type="date" name="fechaNacimiento" id="fechaNacimiento" class="form-control" max="<%= java.time.LocalDate.now().toString() %>" autocomplete="off" onchange="calcularEdadTiempoReal()" required></div>

                        <div class="col-md-2"><label class="form-label small text-secondary fw-semibold">Sexo</label><select name="sexo" id="sexo" class="form-select" required><option value="M">M</option><option value="F">F</option></select></div>

                    </div>



                    <div class="row g-4 mb-5">

                        <div class="col-md-6">

                            <label class="form-label small text-secondary fw-semibold">Enfermedades Preexistentes (Usa Ctrl para elegir varias)</label>

                            <select name="enfermedad" class="form-select" multiple size="4">

                                <option value="Ninguna">Ninguna</option>

                                <% 

                                    List<Map<String, String>> enfermedades = (List<Map<String, String>>) request.getAttribute("listaEnfermedades");

                                    if(enfermedades != null) {

                                        for(Map<String, String> e : enfermedades) {

                                            out.print("<option value='" + e.get("nombre") + "'>" + e.get("nombre") + "</option>");

                                        }

                                    }

                                %>

                            </select>

                        </div>

                        <div class="col-md-6">

                            <label class="form-label small text-secondary fw-semibold">Alergias Conocidas (Usa Ctrl para elegir varias)</label>

                            <select name="alergias" class="form-select" multiple size="4">

                                <option value="Ninguna">Ninguna</option>

                                <% 

                                    List<Map<String, String>> alergias = (List<Map<String, String>>) request.getAttribute("listaAlergias");

                                    if(alergias != null) {

                                        for(Map<String, String> a : alergias) {

                                            out.print("<option value='" + a.get("nombre") + "'>" + a.get("nombre") + " (" + a.get("gravedad") + ")</option>");

                                        }

                                    }

                                %>

                            </select>

                        </div>

                    </div>



                    <h6 class="text-theme pb-2 mb-4" style="border-bottom: 1px solid rgba(255,255,255,0.1);"><i class="bi bi-person-bounding-box me-2 text-primary"></i>Evaluación Antropométrica (IMC)</h6>



                    <div class="row g-4 mb-5 align-items-center">

                        <div class="col-md-3"><label class="form-label small text-secondary fw-semibold">Estatura (m)</label><input type="text" id="estatura" name="estatura" class="form-control" maxlength="4" oninput="formatearEstatura(this)" placeholder="Ej: 1.85" required autocomplete="off"></div>

                        <div class="col-md-3"><label class="form-label small text-secondary fw-semibold">Peso (kg)</label><input type="text" id="peso" name="peso" class="form-control" maxlength="5" oninput="formatearPeso(this)" placeholder="Ej: 75.5" required autocomplete="off"></div>

                        <div class="col-md-6">

                            <div class="imc-box">

                                <i class="bi bi-calculator text-primary fs-2 me-4" style="filter: drop-shadow(0 0 5px var(--accent));"></i>

                                <div><div class="small text-secondary mb-1">Resultado IMC</div><span id="imcValor" class="fw-bold text-theme" style="font-size: 2rem;">0.0</span><span id="imcEstado" class="badge bg-secondary ms-3 px-3 py-2 rounded-pill" style="font-size: 0.9rem;">Sin datos</span></div>

                            </div>

                        </div>

                    </div>



                    <h6 class="text-theme pb-2 mb-4" style="border-bottom: 1px solid rgba(255,255,255,0.1);"><i class="bi bi-heart-pulse text-danger me-2"></i>Signos Vitales</h6>



                    <div class="row g-4">

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Temp (°C)</label>

                            <input type="text" id="temp" name="temperatura" class="form-control" maxlength="4" oninput="formatearTemperatura(this)" placeholder="Ej: 36.5" required autocomplete="off">

                            <div id="alertaTemp" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Presión Arterial (Ej: 120/80)</label>

                            <input type="text" id="presion" name="presion" class="form-control" maxlength="7" oninput="formatearPresion(this)" pattern="\d{2,3}/\d{2,3}" title="Debe usar el formato 120/80" placeholder="Ej: 120/80" required autocomplete="off">

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Frec. Cardiaca (LPM)</label>

                            <input type="text" id="fc" name="fc" class="form-control" oninput="formatearFC(this)" placeholder="Ej: 80" required autocomplete="off">

                            <div id="alertaFc" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Saturación O2 (%)</label>

                            <input type="text" id="sat" name="sat" class="form-control" oninput="formatearSat(this)" placeholder="Ej: 98" required autocomplete="off">

                            <div id="alertaSat" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                    </div>



                    <div class="mt-5 text-end">

                        <button type="button" class="btn btn-secondary px-4 me-2" onclick="cancelarEdicion()"><i class="bi bi-x-circle me-2"></i>Cancelar</button>

                        <button type="submit" class="btn btn-primary px-5"><i class="bi bi-save me-2"></i>Guardar Historia Clínica</button>

                    </div>

                </form>

            </div>

        </div>



        <% } else { %>

        <!-- VISTA DASHBOARD PACIENTE -->

        <div id="dashboard_paciente" class="position-relative" style="z-index: 10;">
        
        <div id="vista-inicio" class="position-relative" style="z-index: 10; display: block !important; opacity: 1 !important; visibility: visible !important;">

            

            <% if(request.getAttribute("mensaje") != null) { %>

                <div class="alert alert-success p-3 text-center mb-4 border-0 rounded-3 shadow-sm" style="background: rgba(16, 185, 129, 0.2); color: #34d399; backdrop-filter: blur(10px);"><i class="bi bi-check-circle me-2"></i><%= request.getAttribute("mensaje") %></div>

            <% } %>

            <% if(request.getAttribute("error") != null) { %>

                <div class="alert alert-danger p-3 text-center mb-4 border-0 rounded-3 shadow-sm" style="background: rgba(239, 68, 68, 0.2); color: #f87171; backdrop-filter: blur(10px);"><i class="bi bi-exclamation-octagon me-2"></i><%= request.getAttribute("error") %></div>

            <% } %>



            <% 

                Paciente miHC = (Paciente) request.getAttribute("miHistoriaClinica");

                if (miHC != null) {

            %>

                        <!-- Jumbotron de Bienvenida (Ahora por fuera de los Datos Clinicos) -->
            <div class="p-5 mb-5 rounded-4 shadow-sm text-white position-relative overflow-hidden" style="background: linear-gradient(135deg, #1e293b, #0f172a); border-left: 5px solid #3b82f6;">
                <!-- Marca de Agua -->
                <i class="bi bi-heart-pulse text-primary position-absolute" style="font-size: 15rem; opacity: 0.05; right: -2%; top: 50%; transform: translateY(-50%) rotate(-15deg); pointer-events: none;"></i>
                
                <div class="container-fluid py-2 position-relative" style="z-index: 2;">
                    <h1 class="display-5 fw-bold mb-3">
                        Bienvenido, <%= (miHC != null && miHC.getNombres() != null) ? miHC.getNombres().split(" ")[0] : "Paciente" %>
                    </h1>
                    <p class="fs-5 text-light opacity-75 mb-4" style="max-width: 800px; line-height: 1.6;">
                        Bienvenido a NurseLogic. Tu ecosistema de salud digital dise&ntilde;ado para darte control total sobre tu historial cl&iacute;nico, facilitar el agendamiento de tus citas y mantener una comunicaci&oacute;n directa con tus especialistas.
                    </p>
                    <button class="btn btn-primary btn-lg rounded-pill px-4 py-3 fw-bold shadow" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'})">
                        <i class="bi bi-calendar-plus me-2"></i>Agendar Nueva Cita
                    </button>
                </div>
            </div>

                                    <!-- Contenedor de Datos Clinicos -->
            <div class="card border-0 mb-5 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <!-- Header -->
                <div class="card-header border-0 px-3 py-3" style="background: rgba(16, 185, 129, 0.05); border-bottom: 1px solid rgba(16, 185, 129, 0.1) !important;">
                    <h5 class="mb-0 fw-bold text-theme d-flex align-items-center">
                        <div class="bg-success bg-opacity-10 rounded-circle p-2 me-2 d-flex align-items-center justify-content-center" style="width: 40px; height: 40px;">
                            <i class="bi bi-clipboard2-pulse-fill text-success fs-4"></i>
                        </div>
                        Mis Datos Cl&iacute;nicos
                    </h5>
                </div>
                
                <div class="card-body p-3 p-md-4">
                    <!-- Datos Personales -->
                    <div class="row g-4 mb-4">
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-person me-2"></i>Nombres Completos</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getNombres() %> <%= miHC.getApellidos() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-card-text me-2"></i>C&eacute;dula</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getCedula() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-calendar3 me-2"></i>Fecha de Nacimiento</label>
                            <div class="fw-bold fs-5 text-theme"><%= (miHC.getFechaNacimiento() != null) ? miHC.getFechaNacimiento() : "Sin registrar" %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-clock-history me-2"></i>&Uacute;ltima Actualizaci&oacute;n</label>
                            <div class="fw-bold fs-5 text-theme"><%= java.time.LocalDate.now().toString() %></div>
                        </div>
                    </div>

                    <!-- Signos Vitales -->
                    <div class="row g-3">
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background-color: rgba(13, 110, 253, 0.05); border: none;">
                                <i class="bi bi-rulers text-primary mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Estatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getEstatura() %><span class="fs-6 fw-normal ms-1 text-muted">m</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background-color: rgba(255, 193, 7, 0.05); border: none;">
                                <i class="bi bi-speedometer2 text-warning mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Peso</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getPeso() %><span class="fs-6 fw-normal ms-1 text-muted">kg</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background-color: rgba(220, 53, 69, 0.05); border: none;">
                                <i class="bi bi-activity text-danger mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Presi&oacute;n</label>
                                <div class="fw-bolder fs-4 text-theme"><%= (miHC.getPresionArterial() != null && !miHC.getPresionArterial().trim().isEmpty()) ? miHC.getPresionArterial() : "--" %></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background-color: rgba(25, 135, 84, 0.05); border: none;">
                                <i class="bi bi-thermometer-half text-success mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Temperatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getTemperatura() %><span class="fs-6 fw-normal ms-1 text-muted">&deg;C</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <% } %>



            <div class="row g-4 mb-4">
                <div class="col-md-7">
                    <div class="form-section mt-0 h-100 d-flex flex-column">
                          <div class="d-flex flex-column flex-grow-1">
                              <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita M&eacute;dica</h4>
                            <p class="text-secondary mb-4">Selecciona la especialidad, fecha y hora para programar tu consulta con nuestros especialistas.</p>
                            <form action="agendarCita" method="post" autocomplete="off" class="d-flex flex-column flex-grow-1">
                                <div class="mb-4">
                                    <label class="form-label small text-secondary fw-semibold">Especialidad</label>
                                    <div class="dropdown">
                                        <input type="hidden" name="especialidad" id="hiddenEspecialidad" required>
                                        <button class="btn form-control form-control-lg border-secondary text-light text-start d-flex justify-content-between align-items-center dropdown-toggle" type="button" id="btnEspecialidad" data-bs-toggle="dropdown" aria-expanded="false" style="background: rgba(0,0,0,0.2);">
                                            <span id="btnEspecialidadText">Elige un &aacute;rea m&eacute;dica...</span>
                                        </button>
                                        <ul class="dropdown-menu w-100 dropdown-menu-dark p-2 shadow-lg border-secondary" style="max-height: 200px; overflow-y: auto;" aria-labelledby="btnEspecialidad">
                                            <li class="position-sticky top-0 bg-dark z-1 pb-2" style="margin-top: -8px; padding-top: 8px;">
                                                <input type="text" id="buscadorEspecialidades" class="form-control form-control-sm border-secondary text-light bg-dark" placeholder="Buscar especialidad..." autocomplete="off">
                                            </li>
                                            <%
                                                List<Map<String, String>> espMapPac = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");
                                                if(espMapPac != null && !espMapPac.isEmpty()) {
                                                    for(Map<String, String> mEsp : espMapPac) {
                                                        out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='" + mEsp.get("id") + "'>" + mEsp.get("descripcion") + "</a></li>");
                                                    }
                                                } else {
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='1'>Medicina General</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='2'>Odontolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='3'>Pediatr&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='4'>Ginecolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='5'>Cardiolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='6'>Urgencias y Triage</a></li>");
                                                }
                                            %>
                                        </ul>
                                    </div>
                                </div>
                                <div class="row g-4">
                                    <div class="col-md-6">
                                        <label class="form-label small text-secondary fw-semibold">Fecha</label>
                                        <input type="date" name="fecha" class="form-control form-control-lg border-secondary text-light" style="background: rgba(0,0,0,0.2); color-scheme: dark;" min="<%= java.time.LocalDate.now().toString() %>" autocomplete="off" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label small text-secondary fw-semibold">Hora</label>
                                        <input type="time" name="hora" class="form-control form-control-lg border-secondary text-light" style="background: rgba(0,0,0,0.2); color-scheme: dark;" required autocomplete="off">
                                    </div>
                                </div>

                                <div class="p-3 mt-3 mb-3 rounded bg-dark border border-secondary text-muted small">
                                    <i class="bi bi-info-circle text-primary me-2"></i><strong>Nota importante:</strong> Por favor, pres&eacute;ntate 15 minutos antes de tu consulta programada. En caso de presentar s&iacute;ntomas graves o emergencias, dir&iacute;gete inmediatamente a nuestra &aacute;rea de Urgencias y Triage.
                                </div>

                                <button type="submit" class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>
<script>
                                document.addEventListener("DOMContentLoaded", function() {
                                    const buscador = document.getElementById("buscadorEspecialidades");
                                    const items = document.querySelectorAll(".especialidad-item");
                                    const hiddenInput = document.getElementById("hiddenEspecialidad");
                                    const btnText = document.getElementById("btnEspecialidadText");

                                    if(buscador) {
                                        buscador.addEventListener("input", function(e) {
                                            const term = this.value.toLowerCase();
                                            items.forEach(item => {
                                                if(item.textContent.toLowerCase().includes(term)) {
                                                    item.style.display = "block";
                                                } else {
                                                    item.style.display = "none";
                                                }
                                            });
                                        });

                                        buscador.addEventListener("click", function(e) {
                                            e.stopPropagation();
                                        });
                                    }

                                    if(hiddenInput && btnText) {
                                        items.forEach(item => {
                                            item.addEventListener("click", function(e) {
                                                e.preventDefault();
                                                hiddenInput.value = this.getAttribute("data-value");
                                                btnText.textContent = this.textContent;
                                                if(buscador) {
                                                    buscador.value = "";
                                                    items.forEach(i => i.style.display = "block");
                                                }
                                            });
                                        });
                                    }
                                });
                            </script>
                            </form>
                        </div>
                    </div>
                </div>

                <div class="col-md-5">
                    <div class="form-section mt-0 d-flex flex-column h-100 justify-content-between">
                        <div>
                            <h4 class="mb-4 fw-bold" style="color: #10b981;"><i class="bi bi-calculator me-2"></i>Calculadora de IMC</h4>
                            <p class="text-secondary mb-4">Conoce tu &Iacute;ndice de Masa Corporal para un mejor seguimiento de tu salud.</p>
                            
                            <div class="mb-4">
                                <label class="form-label small text-secondary fw-semibold">Estatura (metros)</label>
                                <div class="input-group input-group-lg">
                                    <span class="input-group-text border-secondary text-success border-end-0" style="background: rgba(0,0,0,0.3);"><i class="bi bi-rulers"></i></span>
                                    <input type="text" id="estatura_pac" class="form-control border-secondary text-light border-start-0" style="background: rgba(0,0,0,0.15);" maxlength="4" oninput="formatearEstatura_pac(this)" placeholder="Ej: 1.75" required autocomplete="off">
                                </div>
                            </div>
                            <div class="mb-5">
                                <label class="form-label small text-secondary fw-semibold">Peso (kg)</label>
                                <div class="input-group input-group-lg">
                                    <span class="input-group-text border-secondary text-success border-end-0" style="background: rgba(0,0,0,0.3);"><i class="bi bi-speedometer2"></i></span>
                                    <input type="text" id="peso_pac" class="form-control border-secondary text-light border-start-0" style="background: rgba(0,0,0,0.15);" maxlength="5" oninput="formatearPeso_pac(this)" placeholder="Ej: 70.5" required autocomplete="off">
                                </div>
                            </div>
                        </div>

                        <div class="imc-box flex-column align-items-center justify-content-center text-center p-4 mt-auto rounded-4 shadow-sm" style="background: rgba(0,0,0,0.15); border: 1px dashed rgba(16,185,129,0.3);">
                            <div class="small text-secondary mb-2 fw-semibold text-uppercase tracking-wide">Tu Resultado IMC</div>
                            <span id="imcValor_pac" class="fw-bold mb-2" style="font-size: 3.5rem; line-height: 1; color: #10b981;">0.0</span>
                            <span id="imcEstado_pac" class="badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2">Introduce tus datos</span>
                        </div>
                    </div>
                </div>
            </div>



        
        </div> <!-- Fin vista-inicio -->

        <!-- VISTA MIS CITAS PREVIAS -->
        <div id="vista-citas" class="d-none position-relative" style="z-index: 10;">
            <h3 class="fw-bold mb-4" style="color: #f59e0b;"><i class="bi bi-calendar-event me-2"></i>Historial de Citas M&eacute;dicas</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaCitas" style="color-scheme: dark;">
                </div>
                <div class="col-md-8 text-md-end mt-3 mt-md-0 d-flex justify-content-md-end align-items-center">
                    <div class="form-check form-switch m-0">
                        <input class="form-check-input" type="checkbox" id="switchOcultarHistorial" checked>
                        <label class="form-check-label text-muted ms-2" for="switchOcultarHistorial">Ocultar Historial (Atendidos / Cancelados)</label>
                    </div>
                </div>
            </div>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0 w-100" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Horario</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Especialidad</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico Asignado</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <%
                                    List<Map<String, String>> listaCitas = (List<Map<String, String>>) request.getAttribute("listaCitas");
                                    if(listaCitas != null && !listaCitas.isEmpty()) {
                                        for(Map<String, String> cita : listaCitas) {
                                            String estado = cita.get("estado") != null ? cita.get("estado").toUpperCase() : "PENDIENTE";
                                            String badgeClass = "bg-warning text-dark";
                                            if(estado.equals("ATENDIDO")) badgeClass = "bg-success";
                                            else if(estado.equals("CANCELADO")) badgeClass = "bg-danger";
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-clock me-2 text-muted"></i><%= cita.get("fecha") %> <%= cita.get("hora") %></td>
                                    <td class="py-3 px-4"><%= cita.get("especialidad") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= (cita.get("medico") == null || cita.get("medico").equals("null") || cita.get("medico").trim().isEmpty()) ? "<span class=\"text-muted fst-italic\">Por asignar</span>" : cita.get("medico") %></td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="badge rounded-pill <%= badgeClass %>"><%= estado %></span>
                                    </td>
                                </tr>
                                <%
                                        }
                                    } else {
                                %>
                                <tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No tienes citas m&eacute;dicas registradas.</td>
                                </tr>
                                <% } %>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        
        <!-- VISTA RESULTADOS / EXAMENES -->
        <div id="vista-resultados" class="d-none position-relative" style="z-index: 10;">
            <h3 class="fw-bold mb-4" style="color: #a855f7;"><i class="bi bi-file-earmark-medical me-2"></i>Resultados y Ex&aacute;menes Cl&iacute;nicos</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaResultados" style="color-scheme: dark;">
                </div>
            </div>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0 w-100" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Fecha</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Tipo de Examen</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico Solicitante</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <%
                                    List<Map<String, String>> listaResultados = (List<Map<String, String>>) request.getAttribute("listaResultados");
                                    if(listaResultados != null && !listaResultados.isEmpty()) {
                                        for(Map<String, String> res : listaResultados) {
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i><%= res.get("fecha") %></td>
                                    <td class="py-3 px-4"><%= res.get("tipoExamen") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= (res.get("medico") == null || res.get("medico").equals("null") || res.get("medico").trim().isEmpty()) ? "<span class=\"text-muted fst-italic\">Por asignar</span>" : res.get("medico") %></td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-primary"><i class="bi bi-file-earmark-pdf me-2"></i>Ver PDF</button>
                                    </td>
                                </tr>
                                <%
                                        }
                                    } else {
                                %>
                                <tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay resultados registrados.</td>
                                </tr>
                                <% } %>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- VISTA MIS RECETAS -->
        <div id="vista-recetas" class="d-none position-relative" style="z-index: 10;">
            <h3 class="fw-bold mb-4" style="color: #10b981;"><i class="bi bi-capsule me-2"></i>Mis Recetas M&eacute;dicas</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaRecetas" style="color-scheme: dark;">
                </div>
            </div>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0 w-100" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Fecha</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Medicamento / Indicaciones</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <%
                                    List<Map<String, String>> listaRecetas = (List<Map<String, String>>) request.getAttribute("listaRecetas");
                                    if(listaRecetas != null && !listaRecetas.isEmpty()) {
                                        for(Map<String, String> rec : listaRecetas) {
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i><%= rec.get("fecha") %></td>
                                    <td class="py-3 px-4"><%= (rec.get("receta") != null && !rec.get("receta").equals("null")) ? rec.get("receta") : rec.get("diagnostico") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= (rec.get("medico") == null || rec.get("medico").equals("null") || rec.get("medico").trim().isEmpty()) ? "<span class=\"text-muted fst-italic\">Por asignar</span>" : rec.get("medico") %></td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-primary"><i class="bi bi-capsule me-2"></i>Ver Receta</button>
                                    </td>
                                </tr>
                                <%
                                        }
                                    } else {
                                %>
                                <tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay recetas m&eacute;dicas registradas.</td>
                                </tr>
                                <% } %>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

<script>
            


document.addEventListener("DOMContentLoaded", function() {
    let dash = document.getElementById('dashboard_paciente');
    if (dash) {
        dash.classList.remove('d-none');
        dash.style.display = 'block';
        dash.style.opacity = '1';
    }
    let vistaInicioPaciente = document.getElementById('vista-inicio');
    if(vistaInicioPaciente) {
        vistaInicioPaciente.classList.remove('d-none');
        vistaInicioPaciente.style.display = 'block';
    }
});
function switchPacienteTab(tabId) {
                const vistas = ['vista-inicio', 'vista-citas', 'vista-resultados', 'vista-recetas'];
                vistas.forEach(v => {
                    const el = document.getElementById(v);
                    if (el) el.classList.add('d-none');
                });
                const seleccionada = document.getElementById(tabId);
                if (seleccionada) seleccionada.classList.remove('d-none');
            }

            document.addEventListener("DOMContentLoaded", function() {
                let today = new Date().toISOString().split('T')[0];
                const filtros = ['filtroFechaCitas', 'filtroFechaResultados', 'filtroFechaRecetas'];
                filtros.forEach(id => {
                    const input = document.getElementById(id);
                    if(input) input.setAttribute('max', today);
                });
            
                const switchCitas = document.getElementById('switchOcultarHistorial');
                if(switchCitas) {
                    function filtrarHistorial() {
                        const tbody = document.querySelector('#vista-citas tbody');
                        if(!tbody) return;
                        const trs = tbody.querySelectorAll('tr');
                        trs.forEach(tr => {
                            const txt = tr.textContent.toUpperCase();
                            if (txt.includes('ATENDIDO') || txt.includes('CANCELADO') || txt.includes('DESPACHADO')) {
                                if (switchCitas.checked) {
                                    tr.classList.add('d-none');
                                } else {
                                    tr.classList.remove('d-none');
                                }
                            }
                        });
                    }
                    switchCitas.addEventListener('change', filtrarHistorial);
                    filtrarHistorial();
                }
            });
        </script>



        <script>
            function initPacienteParticles() {
                const canvas = document.getElementById('pacienteParticles');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                let width = canvas.width = window.innerWidth;
                let height = canvas.height = window.innerHeight;
                let particles = [];
                
                window.addEventListener('resize', () => {
                    if(window.innerWidth === 0) return;
                    width = canvas.width = window.innerWidth;
                    height = canvas.height = window.innerHeight;
                });

                for (let i = 0; i < 70; i++) {
                    particles.push({
                        x: Math.random() * width,
                        y: Math.random() * height,
                        radius: Math.random() * 4 + 1.5,
                        dx: (Math.random() - 0.5) * 0.5,
                        dy: (Math.random() - 0.5) * 0.5
                    });
                }

                function animate() {
                    requestAnimationFrame(animate);
                    ctx.clearRect(0, 0, width, height);
                    particles.forEach(p => {
                        p.x += p.dx;
                        p.y += p.dy;
                        if (p.x < 0 || p.x > width) p.dx = -p.dx;
                        if (p.y < 0 || p.y > height) p.dy = -p.dy;
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                        ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
                        ctx.fill();
                    });
                }
                animate();
            }
            document.addEventListener("DOMContentLoaded", initPacienteParticles);
        </script>
<% } %>

