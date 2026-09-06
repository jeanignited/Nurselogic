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
%>        <div id="camas" class="vista-activa d-none">

            <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">

                <div>

                    <h3 class="m-0 fw-bold"><i class="bi bi-hospital me-2" style="color: #22d3ee;"></i>Gestión de Camas y Ocupación Hospitalaria</h3>

                    <p class="text-secondary m-0 small">Asignación en tiempo real en Urgencias, Unidad de Cuidados Intensivos (UCI) y Sala General</p>

                </div>

                <div class="d-flex gap-2">

                    <% if(isAdmin) { %>

                    <button class="btn btn-primary text-nowrap rounded-pill px-3 py-2 shadow-sm" data-bs-toggle="modal" data-bs-target="#modalAnadirCama"><i class="bi bi-plus-lg me-1"></i>Añadir Cama</button>

                    <% } %>

                    <a href="exportCsv?tipo=camas" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar Camas</a>

                </div>

            </div>



            <!-- Leyenda de colores -->

            <div class="d-flex gap-4 mb-4 p-3 rounded-3 flex-wrap sub-box">

                <div class="d-flex align-items-center gap-2"><span class="badge bg-success p-2 rounded-circle"></span> <span class="small fw-semibold">Disponible</span></div>

                <div class="d-flex align-items-center gap-2"><span class="badge bg-danger p-2 rounded-circle"></span> <span class="small fw-semibold">Ocupada</span></div>

                <div class="d-flex align-items-center gap-2"><span class="badge bg-warning p-2 rounded-circle"></span> <span class="small fw-semibold">Mantenimiento / Limpieza</span></div>

            </div>



            <%

                List<Map<String, String>> listaCamas = (List<Map<String, String>>) request.getAttribute("listaCamas");

                if (listaCamas == null || listaCamas.isEmpty()) {

            %>

            <div class="text-center py-5 text-secondary">

                <i class="bi bi-hospital fs-1 d-block mb-2"></i>

                <p>No se encontraron camas registradas o no se han cargado desde el Dashboard.</p>

            </div>

            <% } else { %>

            

            <div class="row g-4">

            <%

                String salaActual = "";

                for (Map<String, String> c : listaCamas) {

                    if (!salaActual.equals(c.get("sala"))) {

                        salaActual = c.get("sala");

                        String iconSala = "bi-building";

                        String colorSala = "#38bdf8";

                        if ("Urgencias".equalsIgnoreCase(salaActual)) { iconSala = "bi-exclamation-triangle-fill"; colorSala = "#ef4444"; }

                        else if ("UCI".equalsIgnoreCase(salaActual)) { iconSala = "bi-heart-pulse-fill"; colorSala = "#f59e0b"; }

                        out.println("<div class='col-12 mt-4 mb-1'><h4 class='fw-bold pb-2 border-bottom' style='color: " + colorSala + "; border-color: rgba(255,255,255,0.1) !important;'><i class='bi " + iconSala + " me-2'></i>" + salaActual + "</h4></div>");

                    }

                    String estado = c.get("estado");

                    String bgCard = "rgba(16, 185, 129, 0.1)";

                    String borderCard = "#10b981";

                    String textBadge = "bg-success";

                    if ("Ocupada".equalsIgnoreCase(estado)) {

                        bgCard = "rgba(239, 68, 68, 0.12)";

                        borderCard = "#ef4444";

                        textBadge = "bg-danger";

                    } else if ("Mantenimiento".equalsIgnoreCase(estado)) {

                        bgCard = "rgba(245, 158, 11, 0.12)";

                        borderCard = "#f59e0b";

                        textBadge = "bg-warning text-dark";

                    }

            %>

                <div class="col-md-4 col-lg-3">

                    <div class="p-3 rounded-4 h-100 position-relative shadow-sm d-flex flex-column justify-content-between transition-hover" style="background: <%= bgCard %>; border: 2px solid <%= borderCard %>; backdrop-filter: blur(10px);">

                        <div>

                            <div class="d-flex justify-content-between align-items-center mb-2">

                                <span class="fw-bold fs-5 text-theme"><i class="bi bi-file-medical me-2 text-info"></i><%= c.get("numero") %></span>

                                <span class="badge <%= textBadge %> rounded-pill px-3 py-1"><%= estado %></span>

                            </div>

                            <% if ("Ocupada".equalsIgnoreCase(estado)) { %>

                                <div class="mt-3 small">

                                    <div class="text-theme fw-bold mb-1"><i class="bi bi-person-fill text-danger me-1"></i><%= c.get("paciente") %></div>

                                    <div class="text-secondary"><i class="bi bi-user-md text-info me-1"></i><%= c.get("medico") %></div>

                                    <div class="text-warning mt-1" style="font-size: 0.8rem;"><i class="bi bi-info-circle me-1"></i>Motivo: <%= c.get("motivo") %></div>

                                </div>

                            <% } else if ("Mantenimiento".equalsIgnoreCase(estado)) { %>

                                <div class="mt-3 small text-warning">

                                    <i class="bi bi-tools me-1"></i>En limpieza o desinfección protocolaria.

                                </div>

                            <% } else { %>

                                <div class="mt-3 small text-secondary">

                                    <i class="bi bi-check-circle me-1"></i>Lista para ingreso de nuevo paciente.

                                </div>

                            <% } %>

                        </div>

                        <div class="mt-4 pt-2 border-top d-flex justify-content-between align-items-center" style="border-color: rgba(255,255,255,0.1) !important;">

                            <% if ("Disponible".equalsIgnoreCase(estado)) { %>

                                <button class="btn btn-sm btn-success w-100 fw-semibold rounded-pill shadow-sm" onclick="abrirModalInternar('<%= c.get("id") %>', '<%= c.get("numero") %>', '<%= c.get("sala") %>')"><i class="bi bi-person-plus-fill me-1"></i>Internar Paciente</button>

                            <% } else if ("Ocupada".equalsIgnoreCase(estado)) { %>

                                <button class="btn btn-sm btn-outline-danger flex-grow-1 me-1 rounded-pill" onclick="confirmarAltaCama('<%= c.get("id") %>', '<%= c.get("numero") %>', '<%= c.get("paciente") %>')"><i class="bi bi-box-arrow-right me-1"></i>Dar Alta</button>

                                <button class="btn btn-sm btn-outline-warning rounded-circle" title="Poner en Mantenimiento" onclick="cambiarEstadoCama('<%= c.get("id") %>', 'Mantenimiento')"><i class="bi bi-tools"></i></button>

                            <% } else { %>

                                <button class="btn btn-sm btn-outline-success w-100 rounded-pill" onclick="cambiarEstadoCama('<%= c.get("id") %>', 'Disponible')"><i class="bi bi-check-lg me-1"></i>Habilitar Cama</button>

                            <% } %>

                        </div>

                    </div>

                </div>

            <% } %>

            </div>

            <% } %>

        </div>








