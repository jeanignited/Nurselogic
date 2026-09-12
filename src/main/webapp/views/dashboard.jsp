<%@ page pageEncoding="UTF-8" %>
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

        <div id="dashboard" class="vista-activa">

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

                        <div class="kpi-title"><i class="bi bi-people-fill me-2" style="color: #f59e0b;"></i>Personal Médico</div>

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

                    <i class="bi bi-calendar2-week-fill me-2"></i>Ver Agenda Médica

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

        <div id="dashboard_paciente" class="vista-activa">

            

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

            <div class="form-section mt-0 mb-4 border-start border-4 border-success">

                <h4 class="mb-4 fw-bold" style="color: #10b981;"><i class="bi bi-file-earmark-medical me-2"></i>Mis Datos Clínicos (Registrados por el Médico)</h4>

                <div class="row g-4 text-theme">

                    <div class="col-md-4">

                        <label class="text-secondary small">Nombres Completos</label>

                        <div class="fw-semibold fs-5"><%= miHC.getNombres() %> <%= miHC.getApellidos() %></div>

                    </div>

                    <div class="col-md-4">

                        <label class="text-secondary small">Cédula</label>

                        <div class="fw-semibold fs-5"><%= miHC.getCedula() %></div>

                    </div>

                    <div class="col-md-4">
                        <label class="text-secondary small">Fecha de Nacimiento</label>
                        <div class="fw-semibold fs-5"><%= (miHC.getFechaNacimiento() != null) ? miHC.getFechaNacimiento() : "Sin registrar" %></div>
                    </div>

                    <div class="col-md-3">

                        <label class="text-secondary small">Estatura</label>

                        <div class="fw-semibold fs-5"><%= miHC.getEstatura() %> m</div>

                    </div>

                    <div class="col-md-3">

                        <label class="text-secondary small">Peso</label>

                        <div class="fw-semibold fs-5"><%= miHC.getPeso() %> kg</div>

                    </div>

                    <div class="col-md-3">
                        <label class="text-secondary small">Presión Arterial</label>
                        <div class="fw-semibold fs-5"><%= (miHC.getPresionArterial() != null && !miHC.getPresionArterial().trim().isEmpty()) ? miHC.getPresionArterial() : "Sin evaluar" %></div>
                    </div>

                    <div class="col-md-3">

                        <label class="text-secondary small">Temperatura</label>

                        <div class="fw-semibold fs-5"><%= miHC.getTemperatura() %> °C</div>

                    </div>

                </div>

            </div>

            <% } %>



            <div class="row g-4">

                <div class="col-md-7">

                    <div class="form-section mt-0 h-100 d-flex flex-column">

                        <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita Médica</h4>

                        <p class="text-secondary mb-4">Selecciona la especialidad, fecha y hora para programar tu consulta con nuestros especialistas.</p>

                        <form action="agendarCita" method="post" autocomplete="off">

                            <div class="mb-4">

                                <label class="form-label small text-secondary fw-semibold">Especialidad</label>

                                <select name="especialidad" class="form-select form-select-lg" required>

                                    <option value="" disabled selected>Elige un área médica...</option>

                                    <%

                                        List<Map<String, String>> espMapPac = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");

                                        if(espMapPac != null && !espMapPac.isEmpty()) {

                                            for(Map<String, String> mEsp : espMapPac) {

                                                out.print("<option value='" + mEsp.get("id") + "'>" + mEsp.get("descripcion") + "</option>");

                                            }

                                        } else {

                                            out.print("<option value='1'>Medicina General</option>");

                                            out.print("<option value='2'>Odontología</option>");

                                            out.print("<option value='3'>Pediatría</option>");

                                            out.print("<option value='4'>Ginecología</option>");

                                        }

                                    %>

                                </select>

                            </div>



                            <div class="row g-4 mb-5">

                                <div class="col-md-6">

                                    <label class="form-label small text-secondary fw-semibold">Fecha de la Cita</label>

                                    <input type="date" name="fecha" class="form-control form-control-lg" min="<%= java.time.LocalDate.now().toString() %>" autocomplete="off" required>

                                </div>

                                <div class="col-md-6">

                                    <label class="form-label small text-secondary fw-semibold">Hora</label>

                                    <input type="time" name="hora" class="form-control form-control-lg" required autocomplete="off">

                                </div>

                            </div>



                            <button type="submit" class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>

                        </form>

                    </div>

                </div>



                <div class="col-md-5">

                    <div class="form-section mt-0 h-100 d-flex flex-column">

                        <h4 class="mb-4 fw-bold" style="color: #10b981;"><i class="bi bi-calculator me-2"></i>Calculadora de IMC</h4>

                        <p class="text-secondary mb-4">Conoce tu �ndice de Masa Corporal para un mejor seguimiento de tu salud.</p>

                        

                        <div class="mb-4">

                            <label class="form-label small text-secondary fw-semibold">Estatura (metros)</label>

                            <input type="text" id="estatura_pac" class="form-control form-control-lg" maxlength="4" oninput="formatearEstatura_pac(this)" placeholder="Ej: 1.75" required autocomplete="off">

                        </div>

                        <div class="mb-5">

                            <label class="form-label small text-secondary fw-semibold">Peso (kg)</label>

                            <input type="text" id="peso_pac" class="form-control form-control-lg" maxlength="5" oninput="formatearPeso_pac(this)" placeholder="Ej: 70.5" required autocomplete="off">

                        </div>



                        <div class="imc-box flex-column align-items-center justify-content-center text-center p-4 mt-auto">

                            <div class="small text-secondary mb-2">Tu Resultado IMC</div>

                            <span id="imcValor_pac" class="fw-bold text-theme mb-2" style="font-size: 3.5rem; line-height: 1;">0.0</span>

                            <span id="imcEstado_pac" class="badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2">Introduce tus datos</span>

                        </div>

                    </div>

                </div>

            </div>

        </div>



        <% } %>













