import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace Citas table
citas_table_old = '''<%
                                    List<Map<String, String>> citasPaciente = (List<Map<String, String>>) request.getAttribute("citasPaciente");
                                    if(citasPaciente != null && !citasPaciente.isEmpty()) {
                                        for(Map<String, String> cita : citasPaciente) {
                                            String estado = cita.get("estado") != null ? cita.get("estado").toUpperCase() : "PENDIENTE";
                                            String badgeClass = "bg-warning text-dark";
                                            if(estado.equals("ATENDIDO")) badgeClass = "bg-success";
                                            else if(estado.equals("CANCELADO")) badgeClass = "bg-danger";
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-clock me-2 text-muted"></i><%= cita.get("fecha") %> <%= cita.get("hora") %></td>
                                    <td class="py-3 px-4"><%= cita.get("especialidad") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= cita.get("medico") %></td>
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
                                <% } %>'''

citas_table_new = '''<%
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
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= cita.get("medico") %></td>
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
                                <% } %>'''
c = c.replace(citas_table_old, citas_table_new)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Citas replaced.")
