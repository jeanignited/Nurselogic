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
%>
        <div id="pacientes" class="vista-activa d-none">
            <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
                <h3 class="m-0 fw-bold"><i class="bi bi-folder2-open me-2 text-primary"></i>Base de Datos: Historial Clínico</h3>
                <div class="d-flex align-items-center gap-2" style="width: 100%; max-width: 450px;">
                    <div class="position-relative flex-grow-1">
                        <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>
                        <input type="text" id="buscadorPacientes" class="form-control ps-5" placeholder="Buscar por cédula..." maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" onkeyup="filtrarPacientes()">
                    </div>
                    <a href="exportCsv?tipo=pacientes" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</a>
                </div>
            </div>

            <div class="form-section p-0">
                <div class="table-responsive">
                    <table class="table table-dark-custom table-hover m-0" id="tablaPacientes">
                        <thead><tr><th>Paciente</th><th>Cédula</th><th>Nacimiento</th><% if(isAdmin || permPac){ out.print("<th>Acciónes Clínicas</th>"); } %></tr></thead>
                        <tbody>
                            <%
                                try {
                                    Object objP = request.getAttribute("listaPacientes");
                                    if(objP == null) {
                                        out.print("<tr><td colspan='" + (isAdmin || permPac ? "4" : "3") + "' class='text-center py-5 text-warning'><i class='bi bi-exclamation-triangle me-2'></i>No hay datos. Entra siempre desde /dashboard</td></tr>");
                                    } else if (objP instanceof List) {
                                        List<Map<String, String>> pacientes = (List<Map<String, String>>) objP;
                                        if(pacientes.isEmpty()) {
                                            out.print("<tr><td colspan='" + (isAdmin || permPac ? "4" : "3") + "' class='text-center py-5 text-secondary'><i class='bi bi-inbox me-2 fs-4 d-block mb-2'></i>Sin registros clínicos.</td></tr>");
                                        } else {
                                            for(Map<String, String> p : pacientes) {
                                                out.print("<tr><td class='fw-semibold fs-6'>" + p.get("nombres") + " " + p.get("apellidos") + "</td><td>" + p.get("cedula") + "</td><td>" + p.get("fechaNacimiento") + "</td>");
                                                if(isAdmin || permPac) {
                                                    out.print("<td>");
                                                    out.print("<button type='button' class='btn btn-sm btn-outline-info me-2 mb-1' title='Ficha Médica y Diagnóstico Inteligente' onclick=\"verFichaClinica('" + p.get("cedula") + "')\"><i class='bi bi-eye-fill'></i> Ver Ficha</button>");
                                                    out.print("<button type='button' class='btn btn-sm btn-outline-success me-2 mb-1' title='Prescribir Receta Médica' onclick=\"abrirModalReceta('" + p.get("nombres") + " " + p.get("apellidos") + "', '" + p.get("cedula") + "')\"><i class='bi bi-prescription2'></i> Receta</button>");
                                                    out.print("<button type='button' class='btn btn-sm btn-outline-primary me-2 mb-1' title='Editar Paciente' onclick=\"editarPaciente('" + p.get("cedula") + "')\"><i class='bi bi-pencil'></i></button>");
                                                    if(isAdmin) {
                                                        out.print("<button type='button' class='btn btn-sm btn-outline-danger me-2 mb-1' title='Eliminar Paciente' onclick=\"confirmarBorrado('paciente', '" + p.get("cedula") + "')\"><i class='bi bi-trash'></i></button>");
                                                    }
                                                    out.print("</td>");
                                                }
                                                out.print("</tr>");
                                            }
                                        }
                                    }
                                } catch(Exception e) {}
                            %>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
