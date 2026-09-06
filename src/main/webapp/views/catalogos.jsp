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
%>        <div id="catalogos" class="vista-activa d-none">

            <h3 class="mb-4 fw-bold" style="color: #60a5fa;"><i class="bi bi-folder2-open me-2" style="color: #60a5fa;"></i>Gestor de Catálogos Clínicos Oficiales</h3>

            <div class="row g-4">

                <div class="col-md-6">

                    <div class="form-section h-100 d-flex flex-column">

                        <div class="d-flex justify-content-between align-items-center mb-4">

                            <h4 class="m-0 fw-bold text-danger"><i class="bi bi-heart-pulse-fill me-2"></i>Catálogo de Enfermedades</h4>

                            <% if(isAdmin || permCat) { %>

                            <button type="button" class="btn btn-sm btn-outline-danger" onclick="abrirModalCatalogos('enfermedad')"><i class="bi bi-plus-lg me-1"></i> Nueva Patología</button>

                            <% } %>

                        </div>

                        <div class="table-responsive flex-grow-1">

                            <table class="table table-dark-custom table-hover m-0">

                                <thead><tr><th>Patología / Enfermedad</th><th>Descripción Clínica</th><th>Acciónes</th></tr></thead>

                                <tbody>

                                    <%

                                        List<Map<String, String>> catEnf = (List<Map<String, String>>) request.getAttribute("listaEnfermedades");

                                        if (catEnf == null || catEnf.isEmpty()) {

                                            out.print("<tr><td colspan='3' class='text-center py-4 text-secondary'>No hay enfermedades registradas.</td></tr>");

                                        } else {

                                            for(Map<String, String> ce : catEnf) {

                                                out.print("<tr><td class='fw-bold text-danger-emphasis'>" + ce.get("nombre") + "</td><td class='small text-secondary'>" + (ce.get("descripcion") != null ? ce.get("descripcion") : "Patología clínica") + "</td>");

                                                out.print("<td><div class='d-flex gap-2'><button type='button' class='btn btn-sm btn-outline-info' title='Editar' onclick=\"abrirModalEditarEnfermedad('" + ce.get("id") + "', '" + ce.get("nombre").replace("'", "\\'") + "', '" + (ce.get("descripcion") != null ? ce.get("descripcion").replace("'", "\\'") : "") + "')\"><i class='bi bi-pencil-fill'></i></button><button type='button' class='btn btn-sm btn-outline-danger' title='Eliminar' onclick=\"borrarCatalogo('enfermedad', '" + ce.get("id") + "', '" + ce.get("nombre").replace("'", "\\'") + "')\"><i class='bi bi-trash-fill'></i></button></div></td></tr>");

                                            }

                                        }

                                    %>

                                </tbody>

                            </table>

                        </div>

                    </div>

                </div>

                <div class="col-md-6">

                    <div class="form-section h-100 d-flex flex-column">

                        <div class="d-flex justify-content-between align-items-center mb-4">

                            <h4 class="m-0 fw-bold text-warning"><i class="bi bi-exclamation-diamond-fill me-2"></i>Catálogo de Alergias</h4>

                            <% if(isAdmin || permCat) { %>

                            <button type="button" class="btn btn-sm btn-outline-warning" onclick="abrirModalCatalogos('alergia')"><i class="bi bi-plus-lg me-1"></i> Nuevo Alérgeno</button>

                            <% } %>

                        </div>

                        <div class="table-responsive flex-grow-1">

                            <table class="table table-dark-custom table-hover m-0">

                                <thead><tr><th>Alérgeno</th><th>Gravedad Estándar</th><th>Acciónes</th></tr></thead>

                                <tbody>

                                    <%

                                        List<Map<String, String>> catAle = (List<Map<String, String>>) request.getAttribute("listaAlergias");

                                        if (catAle == null || catAle.isEmpty()) {

                                            out.print("<tr><td colspan='3' class='text-center py-4 text-secondary'>No hay alergias registradas.</td></tr>");

                                        } else {

                                            for(Map<String, String> ca : catAle) {

                                                String grav = ca.get("gravedad");

                                                if (grav == null) grav = "Leve";

                                                if (grav.equalsIgnoreCase("Severa") || grav.equalsIgnoreCase("Severo") || grav.equalsIgnoreCase("Alta") || grav.equalsIgnoreCase("Anafilaxia") || grav.equalsIgnoreCase("Alto")) { grav = "Alto"; }

                                                else if (grav.equalsIgnoreCase("Media") || grav.equalsIgnoreCase("Moderada") || grav.equalsIgnoreCase("Moderado") || grav.equalsIgnoreCase("Medio")) { grav = "Medio"; }

                                                else { grav = "Leve"; }

                                                String bGrav = "Alto".equals(grav) ? "bg-danger" : ("Medio".equals(grav) ? "bg-warning text-dark" : "bg-info text-dark");

                                                out.print("<tr><td class='fw-bold text-warning-emphasis'>" + ca.get("nombre") + "</td><td><span class='badge " + bGrav + " rounded-pill px-3'>" + grav + "</span></td>");

                                                out.print("<td><div class='d-flex gap-2'><button type='button' class='btn btn-sm btn-outline-info' title='Editar' onclick=\"abrirModalEditarAlergia('" + ca.get("id") + "', '" + ca.get("nombre").replace("'", "\\'") + "', '" + grav + "')\"><i class='bi bi-pencil-fill'></i></button><button type='button' class='btn btn-sm btn-outline-danger' title='Eliminar' onclick=\"borrarCatalogo('alergia', '" + ca.get("id") + "', '" + ca.get("nombre").replace("'", "\\'") + "')\"><i class='bi bi-trash-fill'></i></button></div></td></tr>");

                                            }

                                        }

                                    %>

                                </tbody>

                            </table>

                        </div>

                    </div>

                </div>

            </div>

        </div>








