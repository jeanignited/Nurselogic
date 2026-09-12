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
%>        <div id="personal" class="vista-activa d-none">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3 class="m-0 fw-bold"><i class="bi bi-shield-lock me-2 text-warning"></i>Gestión de Personal Médico Registrado</h3>
                <div>
                    <button type="button" class="btn btn-outline-info me-2" data-bs-toggle="modal" data-bs-target="#modalNuevaEspecialidad"><i class="bi bi-award text-info me-2"></i><span class="fw-bold">Crear Especialidad</span></button>
                    <button type="button" class="btn btn-warning" onclick="abrirModalNuevoRol()"><i class="bi bi-plus-circle text-dark me-2"></i><span class="text-dark fw-bold">Crear Nuevo Rol</span></button>
                </div>
            </div>

            <div class="form-section p-0">

                <div class="table-responsive">

                    <table class="table table-dark-custom table-hover m-0">

                        <thead><tr><th>Nombres Completos</th><th>Correo</th><th>Especialidad</th><th>Rol Asignado</th><th>Acciónes</th></tr></thead>

                        <tbody>

                            <%

                                try {

                                    Object objU = request.getAttribute("listaUsuarios");

                                    if(objU == null) {

                                        out.print("<tr><td colspan='5' class='text-center py-5 text-warning'>No hay datos. Entra siempre desde /dashboard</td></tr>");

                                    } else if (objU instanceof List) {

                                        List<Map<String, String>> usuarios = (List<Map<String, String>>) objU;

                                        if(usuarios.isEmpty()) {

                                            out.print("<tr><td colspan='5' class='text-center py-5 text-secondary'><i class='bi bi-people me-2 fs-4 d-block mb-2'></i>No hay personal registrado.</td></tr>");

                                        } else {

                                            for(Map<String, String> u : usuarios) {

                                                String r = u.get("rol");

                                                String esp = u.get("especialidad");

                                                String badge = "Admin".equalsIgnoreCase(r) ? "bg-success" : ("Pendiente".equalsIgnoreCase(r) ? "bg-warning text-dark" : "bg-primary");

                                                String espBadge = (esp != null && !esp.equals("null") && !esp.isEmpty() && !esp.equals("Sin Especialidad")) ? "<span class='badge text-body px-3 py-1'><i class='bi bi-award me-1'></i> " + esp + "</span>" : "<span class='badge px-3 py-1' style='background: rgba(148, 163, 184, 0.2); border: 1px solid rgba(148, 163, 184, 0.4); color: #64748b;'>General</span>";



                                                out.print("<tr>");

                                                out.print("<td class='fw-semibold fs-6'>" + u.get("nombres") + " " + u.get("apellidos") + "</td>");

                                                out.print("<td class='text-secondary'>" + u.get("correo") + "</td>");

                                                out.print("<td>" + espBadge + "</td>");

                                                out.print("<td><span class='badge px-3 py-2 rounded-pill " + badge + "'>" + r + "</span></td>");

                                                out.print("<td>");

                                                out.print("<button class='btn btn-sm btn-outline-warning me-2' title='Asignar Especialidad' onclick=\"abrirModalEspecialidad('" + u.get("correo") + "', '" + esp + "')\"><i class='bi bi-award'></i> Especialidad</button>");

                                                out.print("<button class='btn btn-sm btn-outline-info me-2' title='Cambiar Rol' onclick=\"abrirModalRol('" + u.get("correo") + "', '" + r + "')\"><i class='bi bi-arrow-repeat'></i> Rol</button>");

                                                

                                                if (correoLogueado != null && correoLogueado.equals(u.get("correo"))) {

                                                    out.print("<button class='btn btn-sm btn-outline-secondary' disabled title='No puedes eliminar tu cuenta principal'><i class='bi bi-person-x'></i></button>");

                                                } else {

                                                    out.print("<button class='btn btn-sm btn-outline-danger' onclick=\"confirmarBorrado('usuario', '" + u.get("correo") + "')\"><i class='bi bi-person-x'></i></button>");

                                                }

                                                out.print("</td></tr>");

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








