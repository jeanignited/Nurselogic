<%@ page contentType="text/html;charset=UTF-8" language="java" trimDirectiveWhitespaces="true" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%@ page import="com.nurselogic.model.*" %>
<%
    String rolUsuario = (String) session.getAttribute("rol");
    if(rolUsuario == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    rolUsuario = rolUsuario.trim();
    String correoLogueado = (String) session.getAttribute("correo");
    boolean isAdmin = "Admin".equalsIgnoreCase(rolUsuario);
    boolean isPaciente = "Paciente".equalsIgnoreCase(rolUsuario);
    boolean isFarmaceutico = "Farmaceutico".equalsIgnoreCase(rolUsuario);

    boolean permPac = isAdmin || "Medico".equalsIgnoreCase(rolUsuario) || "Enfermero".equalsIgnoreCase(rolUsuario);
    boolean permMed = isAdmin || "Medico".equalsIgnoreCase(rolUsuario) || isFarmaceutico || "Bodeguero".equalsIgnoreCase(rolUsuario);
    boolean permCat = isAdmin || "Medico".equalsIgnoreCase(rolUsuario);
    boolean canSellStock = isAdmin || isFarmaceutico || "Recepcionista".equalsIgnoreCase(rolUsuario);
    boolean canManageStock = isAdmin || isFarmaceutico || "Bodeguero".equalsIgnoreCase(rolUsuario);
    boolean permCitas = isAdmin || "Medico".equalsIgnoreCase(rolUsuario) || "Recepcionista".equalsIgnoreCase(rolUsuario);
    boolean permUsuarios = isAdmin;

    if("Pendiente".equalsIgnoreCase(rolUsuario)) {
        out.println("<div style='background:#0f172a; color:#fff; height:100vh; display:flex; align-items:center; justify-content:center; font-family:sans-serif;'><div style='text-align:center;'><h2>Acceso Restringido</h2><p>Su cuenta est&aacute; pendiente de revisi&oacute;n.</p><a href='login.jsp' style='color:#3b82f6;'>Volver</a></div></div>");
        return;
    }

    // Store permission flags in request scope for dynamically-included JSPs
    request.setAttribute("isAdmin", isAdmin);
    request.setAttribute("isPaciente", isPaciente);
    request.setAttribute("isFarmaceutico", isFarmaceutico);
    request.setAttribute("permPac", permPac);
    request.setAttribute("permMed", permMed);
    request.setAttribute("permCat", permCat);
    request.setAttribute("canSellStock", canSellStock);
    request.setAttribute("canManageStock", canManageStock);
    request.setAttribute("permCitas", permCitas);
    request.setAttribute("permUsuarios", permUsuarios);
    request.setAttribute("correoLogueado", correoLogueado);
    request.setAttribute("rolUsuario", rolUsuario);
%>
<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <title>NURSELOGIC - Workspace</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root { --bg-main:#0f172a; --bg-panel:rgba(30,41,59,0.7); --text-color:#f8fafc; --accent:#3b82f6; --sidebar-w:260px; --glass-border:1px solid rgba(255,255,255,0.1); }
        html[data-bs-theme="light"] { --bg-main:#f1f5f9; --bg-panel:rgba(255,255,255,0.9); --text-color:#0f172a; --glass-border:1px solid rgba(0,0,0,0.1); }
        body { background-color:var(--bg-main); color:var(--text-color); font-family:'Segoe UI',system-ui,sans-serif; overflow-x:hidden; transition:background-color 0.3s,color 0.3s; }
        .sidebar { width:var(--sidebar-w); height:100vh; background:var(--bg-panel); backdrop-filter:blur(12px); position:fixed; transition:0.3s; border-right:var(--glass-border); z-index:1000; box-shadow:4px 0 15px rgba(0,0,0,0.1); overflow-y:auto; }
        .sidebar.contraida { width:75px; }
        .sidebar.contraida .texto-nav, .sidebar.contraida .brand-title { display:none; }
        .nav-link { color:#94a3b8; padding:12px 25px; margin:4px 12px; border-radius:8px; transition:0.2s; cursor:pointer; display:flex; align-items:center; }
        html[data-bs-theme="light"] .nav-link { color:#64748b; }
        .nav-link:hover, .nav-link.active { color:#fff; background:rgba(59,130,246,0.15); }
        html[data-bs-theme="light"] .nav-link:hover, html[data-bs-theme="light"] .nav-link.active { color:var(--accent); background:rgba(59,130,246,0.1); }
        .nav-link i { font-size:1.2rem; margin-right:15px; }
        .sidebar.contraida .nav-link i { margin-right:0; margin:0 auto; }
        .main-content { margin-left:var(--sidebar-w); transition:0.3s; padding:30px; }
        .main-content.expandida { margin-left:75px; }
        .top-bar { display:flex; justify-content:space-between; margin-bottom:30px; border-bottom:var(--glass-border); padding-bottom:15px; }
        .btn-menu { background:none; border:none; color:var(--text-color); font-size:1.5rem; cursor:pointer; transition:0.3s; }
        .btn-menu:hover { color:var(--accent); }
        .dropdown-menu { background:var(--bg-panel); backdrop-filter:blur(15px); border:var(--glass-border); }
        .dropdown-item { color:var(--text-color); transition:0.2s; }
        .dropdown-item:hover { color:#fff; background-color:var(--accent); }
        .glass-card { background:var(--bg-panel); backdrop-filter:blur(12px); border:var(--glass-border); border-radius:12px; box-shadow:0 4px 6px rgba(0,0,0,0.05); transition:transform 0.2s,box-shadow 0.2s; }
        .kpi-card { background:var(--bg-panel); border:var(--glass-border); border-radius:12px; padding:25px; transition:transform 0.2s,box-shadow 0.2s; cursor:pointer; box-shadow:0 4px 6px rgba(0,0,0,0.05); }
        .kpi-card:hover { transform:translateY(-5px); box-shadow:0 10px 20px rgba(0,0,0,0.1); }
        .kpi-title { font-size:0.85rem; color:#94a3b8; text-transform:uppercase; letter-spacing:1px; }
        html[data-bs-theme="light"] .kpi-title { color:#64748b; }
        .kpi-number { font-size:3rem; font-weight:bold; color:var(--text-color); }
        .form-section { background:var(--bg-panel); padding:30px; border-radius:12px; border:var(--glass-border); margin-top:30px; box-shadow:0 10px 30px rgba(0,0,0,0.3); }
        .form-control, .form-select { background:rgba(15,23,42,0.6); border:var(--glass-border); color:#fff; border-radius:8px; padding:12px 15px; transition:0.3s; }
        .form-control:focus, .form-select:focus { background:rgba(15,23,42,0.9); color:#fff; border-color:var(--accent); box-shadow:0 0 0 4px rgba(59,130,246,0.15); }
        html[data-bs-theme="light"] .form-control, html[data-bs-theme="light"] .form-select { background:#ffffff!important; border:1px solid #cbd5e1!important; color:#0f172a!important; box-shadow:0 1px 2px rgba(0,0,0,0.05)!important; }
        html[data-bs-theme="light"] .form-control:focus, html[data-bs-theme="light"] .form-select:focus { background:#ffffff!important; color:#0f172a!important; border-color:#0284c7!important; box-shadow:0 0 0 3px rgba(14,165,233,0.2)!important; }
        .table-dark-custom { --bs-table-bg:transparent; --bs-table-color:var(--text-color); --bs-table-hover-color:var(--text-color); --bs-table-hover-bg:rgba(255,255,255,0.05); border-color:rgba(255,255,255,0.05); }
        html[data-bs-theme="light"] .table-dark-custom { --bs-table-bg:transparent; --bs-table-color:#0f172a; --bs-table-hover-color:#0f172a; --bs-table-hover-bg:rgba(0,0,0,0.05); border-color:rgba(0,0,0,0.05); }
        .sub-box { background:rgba(0,0,0,0.2); border:var(--glass-border); border-radius:8px; padding:15px; }
        html[data-bs-theme="light"] .sub-box { background:rgba(0,0,0,0.03); }
        .imc-box { background:rgba(0,0,0,0.2); border:var(--glass-border); border-radius:8px; padding:15px; display:flex; align-items:center; height:100%; }
        html[data-bs-theme="light"] .imc-box { background:rgba(0,0,0,0.03); }
        .fade-in { animation:fadeIn 0.4s ease-in-out; }
        @keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
        .text-theme { color:var(--text-color)!important; }
        ::-webkit-scrollbar { width:8px; }
        ::-webkit-scrollbar-track { background:var(--bg-main); }
        ::-webkit-scrollbar-thumb { background:#475569; border-radius:4px; }
        ::-webkit-scrollbar-thumb:hover { background:#64748b; }
        .modal-backdrop { z-index:1040!important; }
        .modal { z-index:1050!important; }
        [data-bs-theme="dark"] ::placeholder { color:#94a3b8!important; opacity:1; }
    </style>
</head>
<body>
    <form id="formAdminAction" action="adminAction" method="POST" style="display:none;">
        <input type="hidden" name="action" id="adminActionType">
        <input type="hidden" name="target" id="adminActionTarget">
        <input type="hidden" name="id" id="adminActionId">
    </form>

    <jsp:include page="includes/sidebar.jsp" />

    <div class="main-content" id="main-content">
        <jsp:include page="includes/topbar.jsp" />

        <!-- Vistas Modulares -->
        <jsp:include page="views/dashboard.jsp" />
        <jsp:include page="views/estadisticas.jsp" />
        <jsp:include page="views/camas.jsp" />
        <jsp:include page="views/pacientes.jsp" />
        <jsp:include page="views/medicamentos.jsp" />
        <jsp:include page="views/catalogos.jsp" />
        <jsp:include page="views/facturas.jsp" />
        <jsp:include page="views/personal.jsp" />
        <jsp:include page="views/reportes.jsp" />
        <jsp:include page="views/agenda.jsp" />
    </div>

    <!-- Modales Globales -->
    <jsp:include page="includes/modals.jsp" />

    <!-- Scripts -->
    <jsp:include page="includes/scripts.jsp" />
</body>
</html>