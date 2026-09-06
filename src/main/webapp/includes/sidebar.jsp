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
    <nav class="sidebar" id="sidebar">

        <div class="p-4 d-flex align-items-center mb-2" style="border-bottom: var(--glass-border); flex-shrink: 0;">

            <i class="bi bi-activity text-primary fs-3 me-3" style="filter: drop-shadow(0 0 8px var(--accent));"></i>

            <span class="brand-title fw-bold fs-5 tracking-wide">NURSELOGIC</span>

        </div>

        <ul class="nav flex-column flex-nowrap overflow-y-auto" style="display: flex; flex-direction: column; flex-grow: 1; height: 100%;">

            <% if(!isPaciente) { %>

            <li class="nav-item"><a class="nav-link active" onclick="cambiarVista('dashboard')"><i class="bi bi-grid-1x2 text-primary"></i><span class="texto-nav">Dashboard</span></a></li>

            <% if(!isFarmaceutico) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('estadisticas')"><i class="bi bi-graph-up-arrow" style="color: #c084fc;"></i><span class="texto-nav">Estadisticas</span></a></li>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('camas')"><i class="bi bi-hospital" style="color: #22d3ee;"></i><span class="texto-nav">Hospitalizacion y Camas</span></a></li>

            <% } %>

            <% } %>

            <% if(permPac) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('pacientes')"><i class="bi bi-people text-info"></i><span class="texto-nav">Directorio Pacientes</span></a></li>

            <% } %>

            <% if(permMed) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('medicamentos')"><i class="bi bi-capsule text-success"></i><span class="texto-nav">Inventario Farmacos</span></a></li>

            <% } %>

            <% if(permCat) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('catalogos')"><i class="bi bi-folder2-open" style="color: #60a5fa;"></i><span class="texto-nav">Catalogos Clinicos</span></a></li>

            <% } %>



            <% if(canSellStock) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('facturas')"><i class="bi bi-receipt text-primary"></i><span class="texto-nav">Reporte de Ventas</span></a></li>

            <% } %>



            <% if(permCitas && !isPaciente) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('agenda')"><i class="bi bi-calendar-check text-warning"></i><span class="texto-nav">Agenda Medica</span></a></li>

            <% } %>



            <% if(isPaciente) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('dashboard_paciente')"><i class="bi bi-calendar-heart text-danger"></i><span class="texto-nav">Agendar Cita</span></a></li>

            <% } %>



            <% if(permUsuarios) { %>

            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('personal')"><i class="bi bi-shield-lock" style="color: #34d399;"></i><span class="texto-nav">Personal Medico</span></a></li>

            <% } %>



            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('reportes')"><i class="bi bi-headset" style="color: #fbbf24;"></i><span class="texto-nav">Soporte T.I.</span></a></li>

            <li class="nav-item mt-auto pt-4 pb-4"><a class="nav-link" href="login.jsp"><i class="bi bi-box-arrow-left" style="color: #ef4444;"></i><span class="texto-nav">Cerrar Sesion</span></a></li>

        </ul>

    </nav>






