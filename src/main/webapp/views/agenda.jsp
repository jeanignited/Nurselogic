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
%>        <div id="agenda" class="vista-activa d-none">
            <div class="form-section mt-5" id="seccionAgendaMedica">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h4 class="m-0 fw-bold" style="color: #38bdf8;"><i class="bi bi-calendar2-check me-2" style="color: #38bdf8;"></i>Agenda Médica y Citas Programadas</h4>
                    <div class="d-flex align-items-center gap-2 flex-wrap">
                        <button type="button" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV" onclick="exportarCitasFechas()"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</button>
                        <button type="button" class="btn btn-sm btn-outline-info rounded-pill px-3 py-2 shadow-sm" onclick="abrirModalReceta('')"><i class="bi bi-prescription2 me-1"></i>Prescribir Receta</button>
                        <span class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-2 disabled" style="opacity: 1;"><i class="bi bi-clock me-2"></i>Turnos y Citas del Día</span>
                        <% if(isAdmin || permCitas) { %>
                        <button type="button" class="btn btn-sm px-3 py-2 fw-bold shadow-sm" style="background: linear-gradient(135deg, #38bdf8, #0ea5e9); color: #0b0f19; border:none; border-radius: 8px;" onclick="abrirModalCitaAdmin()"><i class="bi bi-calendar-plus me-1"></i> + Agendar Cita</button>
                        <% } %>
                    </div>
                </div>
                <div class="row mb-3 g-2 align-items-center">
                    <div class="col-md-4 position-relative">
                        <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>
                        <input type="text" id="buscadorCitas" class="form-control ps-5 form-control-sm" placeholder="Buscar cédula, paciente o estado..." onkeyup="filtrarCitasAvanzado()" autocomplete="off">
                    </div>
                    <div class="col-md-3">
                        <input type="date" id="filtroFechaCitas" class="form-control form-control-sm text-secondary" onchange="filtrarCitasAvanzado()" autocomplete="off">
                    </div>
                    <div class="col-md-5">
                        <div class="form-check form-switch d-flex align-items-center gap-2 ms-2">
                            <input class="form-check-input mt-0" type="checkbox" id="checkOcultarCerradas" checked onchange="filtrarCitasAvanzado()" style="cursor: pointer;" autocomplete="off">
                            <label class="form-check-label text-secondary small mb-0" for="checkOcultarCerradas" style="cursor: pointer; padding-top: 2px;">Ocultar Historial (Atendidos / Cancelados)</label>
                        </div>
                    </div>
                </div>
                <div class="table-responsive">
                    <table id="tablaCitas" class="table table-dark-custom table-hover m-0">
                        <thead>
                            <tr>
                                <th>Horario</th>
                                <th>Paciente</th>
                                <th>Especialidad</th>
                                <th>Estado</th>
                                <% if(isAdmin || permCitas) { out.print("<th>Acciónes Médicas</th>"); } %>
                            </tr>
                        </thead>
                        <tbody>
                            <%
                                List<Map<String, String>> citasDash = (List<Map<String, String>>) request.getAttribute("listaCitas");
                                if (citasDash == null || citasDash.isEmpty()) {
                                    out.print("<tr><td colspan='" + (isAdmin || permCitas ? "5" : "4") + "' class='text-center py-5 text-secondary'><i class='bi bi-calendar-x me-2 fs-4 d-block mb-2'></i>No hay citas agendadas por el momento.</td></tr>");
                                } else {
                                    for(Map<String, String> c : citasDash) {
                                        String estBadge = "bg-secondary";
                                        String estIcon = "bi-clock";
                                        if ("ATENDIDO".equalsIgnoreCase(c.get("estado"))) { estBadge = "bg-success"; estIcon = "bi-check-circle-fill"; }
                                        else if ("CANCELADO".equalsIgnoreCase(c.get("estado"))) { estBadge = "bg-danger"; estIcon = "bi-x-circle-fill"; }
                                        else if ("EN SALA".equalsIgnoreCase(c.get("estado"))) { estBadge = "bg-warning text-dark"; estIcon = "bi-person-badge"; }

                                        out.print("<tr>");
                                        out.print("<td class='fw-bold text-info'><i class='bi bi-clock me-1'></i>" + c.get("hora") + "<br><small class='text-secondary fw-normal'>" + c.get("fecha") + "</small></td>");
                                        out.print("<td class='fw-semibold fs-6'>" + c.get("paciente") + "</td>");
                                        out.print("<td><span class='badge text-body px-3 py-1'>" + c.get("especialidad") + "</span></td>");
                                        out.print("<td><span class='badge " + estBadge + " rounded-pill px-3 py-2 fs-6'><i class='bi " + estIcon + " me-1'></i>" + c.get("estado") + "</span></td>");
                                        if (isAdmin || permCitas) {
                                            out.print("<td>");
                                            if (!"ATENDIDO".equalsIgnoreCase(c.get("estado")) && !"CANCELADO".equalsIgnoreCase(c.get("estado"))) {
                                                out.print("<div class='btn-group' role='group'>");
                                                out.print("<button type='button' class='btn btn-sm btn-outline-info' title='Prescribir Receta' onclick=\"abrirModalReceta('" + c.get("paciente") + "', '" + c.get("cedula") + "')\"><i class='bi bi-prescription2'></i></button>");
                                                out.print("<button type='button' class='btn btn-sm btn-outline-success' title='Realizar Consulta Médica' onclick=\"abrirModalAtenderCita(" + c.get("id") + ", '" + c.get("paciente") + "')\"><i class='bi bi-heart-pulse-fill'></i> Atender</button>");
                                                out.print("<button type='button' class='btn btn-sm btn-outline-warning' title='Marcar en Sala' onclick=\"cambiarEstadoCita(" + c.get("id") + ", 'EN SALA')\"><i class='bi bi-person-badge'></i> En Sala</button>");
                                                out.print("<button type='button' class='btn btn-sm btn-outline-danger' title='Cancelar Cita' onclick=\"cambiarEstadoCita(" + c.get("id") + ", 'CANCELADO')\"><i class='bi bi-x-lg'></i></button>");
                                                out.print("</div>");
                                            } else {
                                                out.print("<div class='d-flex align-items-center gap-2'>");
                                                if ("ATENDIDO".equalsIgnoreCase(c.get("estado"))) {
                                                    out.print("<button type='button' class='btn btn-sm btn-outline-info' title='Ver Diagnóstico' onclick=\"abrirModalVerDiagnostico('" + c.get("paciente") + "', this)\" data-diagnostico=\"" + c.get("diagnostico").replace("\"", "&quot;") + "\" data-receta=\"" + c.get("receta").replace("\"", "&quot;") + "\"><i class='bi bi-file-medical'></i> Diagnóstico</button>");
                                                }
                                                if (isAdmin) {
                                                    out.print("<button type='button' class='btn btn-sm btn-outline-danger' title='Eliminar Cita del Historial' onclick=\"confirmarBorrado('cita', '" + c.get("id") + "')\"><i class='bi bi-trash'></i> Eliminar</button>");
                                                } else if ("CANCELADO".equalsIgnoreCase(c.get("estado"))) {
                                                    out.print("<span class='text-secondary small'><i class='bi bi-x-circle me-1'></i>Cancelado</span>");
                                                }
                                                out.print("</div>");
                                            }
                                            out.print("</td>");
                                        }
                                        out.print("</tr>");
                                    }
                                }
                            %>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>








