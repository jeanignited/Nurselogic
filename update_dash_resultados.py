import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

resultados_old = '''<tr>
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i>2026-09-12</td>
                                    <td class="py-3 px-4">Hemograma Completo</td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i>Dr. Carlos M.</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-primary rounded-pill px-3"><i class="bi bi-file-earmark-pdf me-2"></i>Ver PDF</button>
                                    </td>
                                </tr>'''

resultados_new = '''<%
                                    List<Map<String, String>> listaResultados = (List<Map<String, String>>) request.getAttribute("listaResultados");
                                    if(listaResultados != null && !listaResultados.isEmpty()) {
                                        for(Map<String, String> res : listaResultados) {
                                %>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i><%= res.get("fecha") %></td>
                                    <td class="py-3 px-4"><%= res.get("tipoExamen") %></td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i><%= res.get("medico") %></td>
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
                                <% } %>'''

c = c.replace(resultados_old, resultados_new)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Resultados replaced.")
