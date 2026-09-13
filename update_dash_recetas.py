import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

recetas_old = '''<tr>
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i>2026-09-10</td>
                                    <td class="py-3 px-4">Faringitis Aguda</td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i>Dra. Ana V.</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-success rounded-pill px-3"><i class="bi bi-capsule me-2"></i>Ver Receta</button>
                                    </td>
                                </tr>'''

recetas_new = '''<%
                                    List<Map<String, String>> listaRecetas = (List<Map<String, String>>) request.getAttribute("listaRecetas");
                                    if(listaRecetas != null && !listaRecetas.isEmpty()) {
                                        for(Map<String, String> rec : listaRecetas) {
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i><%= rec.get("fecha") %></td>
                                    <td class="py-3 px-4"><%= rec.get("diagnostico") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= rec.get("medico") %></td>
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
                                <% } %>'''

c = c.replace(recetas_old, recetas_new)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Recetas replaced.")
