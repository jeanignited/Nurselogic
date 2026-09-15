import io

with io.open('src/main/webapp/views/personal.jsp', 'r', encoding='utf-8') as f:
    personal = f.read()

roles_table = """
            <div class="d-flex justify-content-between align-items-center mt-5 mb-4">
                <h3 class="m-0 fw-bold"><i class="bi bi-person-badge me-2 text-warning"></i>Roles Creados en el Sistema</h3>
            </div>
            <div class="form-section p-0">
                <div class="table-responsive">
                    <table class="table table-dark-custom table-hover m-0">
                        <thead><tr><th>ID</th><th>Nombre del Rol</th><th>Descripcion</th><th>Permisos Legacy</th><th>Acciones</th></tr></thead>
                        <tbody>
                            <%
                                try {
                                    List<Rol> rolesObj = (List<Rol>) request.getAttribute("listaRolesObj");
                                    if(rolesObj != null && !rolesObj.isEmpty()) {
                                        for(Rol rObj : rolesObj) {
                                            out.print("<tr>");
                                            out.print("<td class='fw-semibold'>ROL-" + rObj.getId() + "</td>");
                                            out.print("<td class='fw-bold'>" + rObj.getNombre() + "</td>");
                                            out.print("<td class='text-secondary'>" + (rObj.getDescripcion() != null ? rObj.getDescripcion() : "") + "</td>");
                                            out.print("<td class='text-secondary'>" + (rObj.getPermisos() != null ? rObj.getPermisos() : "") + "</td>");
                                            out.print("<td>");
                                            out.print("<button class='btn btn-sm btn-outline-danger' onclick=\"confirmarBorrado('rol', '" + rObj.getId() + "')\"><i class='bi bi-trash'></i></button>");
                                            out.print("</td></tr>");
                                        }
                                    } else {
                                        out.print("<tr><td colspan='5' class='text-center py-5 text-secondary'>No hay roles registrados.</td></tr>");
                                    }
                                } catch(Exception e) {}
                            %>
                        </tbody>
                    </table>
                </div>
            </div>
"""

personal = personal.replace('</div>\n\n\n\n\n\n\n', '</div>\n' + roles_table + '\n')

with io.open('src/main/webapp/views/personal.jsp', 'w', encoding='utf-8') as f:
    f.write(personal)
