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
%>        <div class="top-bar">

            <button class="btn-menu" onclick="toggleMenu()"><i class="bi bi-list"></i></button>

            <div class="text-end d-flex align-items-center gap-3">

                <!-- Alertas Inteligentes (Campana) -->

                <% if(!isPaciente) { %>

                <% 

                   int totalAlertasM = (request.getAttribute("alertasMeds") != null) ? (Integer) request.getAttribute("alertasMeds") : 0;

                   int totalAlertasC = (request.getAttribute("alertasCamas") != null) ? (Integer) request.getAttribute("alertasCamas") : 0;

                   int totalAlertasCi = (request.getAttribute("alertasCitas") != null) ? (Integer) request.getAttribute("alertasCitas") : 0;

                   int sumaAlertas = totalAlertasM + totalAlertasC + totalAlertasCi;

                %>

                <div class="dropdown">

                    <button class="btn btn-sm btn-outline-secondary position-relative d-flex align-items-center justify-content-center rounded-circle shadow-sm" type="button" id="notifDropdown" data-bs-toggle="dropdown" aria-expanded="false" style="width: 40px; height: 40px; background: var(--bg-panel); backdrop-filter: blur(10px); border: var(--glass-border); color: inherit;">

                        <i class="bi bi-bell-fill text-warning fs-6"></i>

                        <% if (sumaAlertas > 0) { %>

                        <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" style="font-size: 0.65rem;"><%= sumaAlertas %></span>

                        <% } %>

                    </button>

                    <ul class="dropdown-menu dropdown-menu-end shadow-lg rounded-4 border-0 p-3" aria-labelledby="notifDropdown" style="width: 320px; background: var(--bg-panel); backdrop-filter: blur(20px); border: var(--glass-border); color: inherit;">

                        <li class="d-flex justify-content-between align-items-center mb-2 border-bottom pb-2" style="border-color: rgba(255,255,255,0.1) !important;">

                            <span class="fw-bold small"><i class="bi bi-bell-fill text-warning me-2"></i>Alertas de Hospital</span>

                            <span class="badge bg-danger rounded-pill"><%= sumaAlertas %> Nuevas</span>

                        </li>

                        <% if (totalAlertasM > 0) { %>

                        <li>

                            <a class="dropdown-item p-2 rounded-3 mb-1 text-wrap small d-flex align-items-start gap-2" href="#" onclick="cambiarVista('medicamentos'); return false;" style="color: inherit;">

                                <i class="bi bi-exclamation-triangle-fill text-danger fs-5 mt-1"></i>

                                <div>

                                    <div class="fw-bold text-danger">Stock Crítico en Inventario</div>

                                    <div class="text-secondary" style="font-size: 0.75rem;">Hay <%= totalAlertasM %> medicamento(s) con menos de 10 unidades.</div>

                                </div>

                            </a>

                        </li>

                        <% } %>

                        <% if (totalAlertasC > 0) { %>

                        <li>

                            <a class="dropdown-item p-2 rounded-3 mb-1 text-wrap small d-flex align-items-start gap-2" href="#" onclick="cambiarVista('camas'); return false;" style="color: inherit;">

                                <i class="bi bi-hospital-fill text-info fs-5 mt-1"></i>

                                <div>

                                    <div class="fw-bold text-info">Ocupación Hospitalaria</div>

                                    <div class="text-secondary" style="font-size: 0.75rem;">Hay <%= totalAlertasC %> cama(s) actualmente ocupada(s).</div>

                                </div>

                            </a>

                        </li>

                        <% } %>

                        <% if (totalAlertasCi > 0) { %>

                        <li>

                            <a class="dropdown-item p-2 rounded-3 text-wrap small d-flex align-items-start gap-2" href="#" onclick="cambiarVista('dashboard'); return false;" style="color: inherit;">

                                <i class="bi bi-calendar-check-fill text-success fs-5 mt-1"></i>

                                <div>

                                    <div class="fw-bold text-success">Citas de Hoy</div>

                                    <div class="text-secondary" style="font-size: 0.75rem;">Hay <%= totalAlertasCi %> paciente(s) con citas agendadas hoy.</div>

                                </div>

                            </a>

                        </li>

                        <% } %>

                        <% if (sumaAlertas == 0) { %>

                        <li>

                            <div class="p-2 text-center text-secondary small">

                                No hay nuevas alertas.

                            </div>

                        </li>

                        <% } %>

                    </ul>

                </div>

                <% } %>



                <!-- Widget Selector de Tema Dashboard -->

                <div class="dropdown">

                    <button class="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-2 px-3 py-2 rounded-pill shadow-sm" type="button" id="themeDropdownDash" data-bs-toggle="dropdown" aria-expanded="false" style="background: var(--bg-panel); backdrop-filter: blur(10px); border: var(--glass-border); color: inherit;">

                        <i class="bi bi-moon-stars-fill" id="themeIconDash"></i>

                        <span id="themeLabelDash" class="small fw-semibold">Oscuro</span>

                    </button>

                    <ul class="dropdown-menu dropdown-menu-end shadow-lg rounded-3 border-0" aria-labelledby="themeDropdownDash" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">

                        <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('dark'); return false;"><i class="bi bi-moon-stars-fill text-primary"></i> Modo Oscuro</a></li>

                        <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('light'); return false;"><i class="bi bi-sun-fill text-warning"></i> Modo Claro</a></li>

                        <li><hr class="dropdown-divider border-secondary opacity-25"></li>

                        <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('auto'); return false;"><i class="bi bi-display text-info"></i> Sistema (Auto)</a></li>

                    </ul>

                </div>



                <div class="me-3 text-end">

                    <small class="text-secondary d-block" style="font-size: 0.75rem; letter-spacing: 1px; text-transform: uppercase;">Módulo Activo</small>

                    <%

                       String nombreTop = (String) session.getAttribute("nombres");

                       if(nombreTop == null || nombreTop.trim().isEmpty() || nombreTop.contains("null")) {

                           nombreTop = "Usuario del Sistema";

                       }

                    %>

                    <span class="fw-bold" style="font-size: 1.1rem;"><%= nombreTop %></span>

                    <span class="badge bg-primary ms-2 rounded-pill"><%= rolUsuario %></span>

                </div>

                <div class="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center" style="width: 45px; height: 45px; font-weight: bold; font-size: 1.2rem; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);">

                    <%= nombreTop.substring(0, 1).toUpperCase() %>

                </div>

            </div>

        </div>










