# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Wrap the current content in <div id="vista-inicio">
start_tag = '<div id="dashboard_paciente" class="vista-activa">'
start_idx = c.find(start_tag) + len(start_tag)
c = c[:start_idx] + '\n        <div id="vista-inicio">' + c[start_idx:]

# 2. End vista-inicio, add vista-citas, and scripts right before <% } %>
end_tag = '<% } %>'
end_idx = c.rfind(end_tag)

new_views = u'''
        </div> <!-- Fin vista-inicio -->

        <!-- VISTA MIS CITAS PREVIAS -->
        <div id="vista-citas" class="d-none">
            <h3 class="fw-bold mb-4" style="color: #f59e0b;"><i class="bi bi-calendar-event me-2"></i>Historial de Citas M&eacute;dicas</h3>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Horario</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Especialidad</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico Asignado</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <%
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
                                <% } %>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function switchPacienteTab(tabId) {
                // Ocultar todas las vistas del paciente
                const vistaInicio = document.getElementById('vista-inicio');
                const vistaCitas = document.getElementById('vista-citas');
                
                if (vistaInicio) vistaInicio.classList.add('d-none');
                if (vistaCitas) vistaCitas.classList.add('d-none');
                
                // Mostrar solo la seleccionada
                const seleccionada = document.getElementById(tabId);
                if (seleccionada) {
                    seleccionada.classList.remove('d-none');
                } else if (tabId === 'vista-resultados' || tabId === 'vista-recetas') {
                    // Fallback para las vistas pendientes
                    if (vistaInicio) vistaInicio.classList.remove('d-none');
                    Swal.fire({
                        icon: 'info',
                        title: 'Pr&oacute;ximamente',
                        text: 'Este m&oacute;dulo estar&aacute; disponible muy pronto.',
                        background: 'var(--bg-panel)',
                        color: '#fff',
                        confirmButtonColor: '#3b82f6'
                    });
                }
                
                // Si el menu de bootstrap esta abierto en movil, podemos intentar cerrarlo si existe (opcional)
            }
        </script>

'''

c = c[:end_idx] + new_views + c[end_idx:]

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp updated.")
