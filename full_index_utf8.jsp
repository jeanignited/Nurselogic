<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%
    String rolUsuario = (String) session.getAttribute("rol");
    if(rolUsuario == null) {
        response.sendRedirect("login.jsp");
        return;
    }

    rolUsuario = rolUsuario.trim();
    boolean isAdmin = "Admin".equalsIgnoreCase(rolUsuario);

    if("Pendiente".equalsIgnoreCase(rolUsuario)) {
        out.println("<div style='background:#0f172a; color:#fff; height:100vh; display:flex; align-items:center; justify-content:center; font-family:sans-serif;'><div style='text-align:center;'><h2>Acceso Restringido</h2><p>Su cuenta est├í pendiente de revisi├│n.</p><a href='login.jsp' style='color:#3b82f6;'>Volver</a></div></div>");
        return;
    }
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>NURSELOGIC - Workspace</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <style>
        :root { --bg-main: #0f172a; --bg-panel: #1e293b; --text-color: #f8fafc; --accent: #3b82f6; --sidebar-w: 260px; }
        body { background-color: var(--bg-main); color: var(--text-color); font-family: 'Segoe UI', system-ui, sans-serif; overflow-x: hidden; }
        .sidebar { width: var(--sidebar-w); height: 100vh; background: var(--bg-panel); position: fixed; transition: 0.3s; border-right: 1px solid #334155; z-index: 1000; }
        .sidebar.contraida { width: 75px; }
        .sidebar.contraida .texto-nav, .sidebar.contraida .brand-title { display: none; }
        .nav-link { color: #94a3b8; padding: 15px 25px; transition: 0.2s; border-left: 3px solid transparent; cursor: pointer; display: flex; align-items: center; }
        .nav-link:hover, .nav-link.active { color: #fff; background: #334155; border-left-color: var(--accent); }
        .nav-link i { font-size: 1.3rem; margin-right: 15px; }
        .sidebar.contraida .nav-link i { margin-right: 0; margin: 0 auto; }
        .main-content { margin-left: var(--sidebar-w); transition: 0.3s; padding: 30px; }
        .main-content.expandida { margin-left: 75px; }
        .top-bar { display: flex; justify-content: space-between; margin-bottom: 30px; border-bottom: 1px solid #334155; padding-bottom: 15px; }
        .btn-menu { background: none; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; }
        .kpi-card { background: var(--bg-panel); border: 1px solid #334155; border-radius: 8px; padding: 25px; transition: transform 0.2s; cursor: pointer; }
        .kpi-card:hover { transform: translateY(-5px); }
        .kpi-title { font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }
        .kpi-number { font-size: 3rem; font-weight: bold; color: #fff; }
        .form-section { background: var(--bg-panel); padding: 30px; border-radius: 8px; border: 1px solid #334155; margin-top: 30px; }
        .form-control, .form-select { background: #0f172a; border: 1px solid #334155; color: #fff; }
        .form-control:focus, .form-select:focus { background: #0f172a; color: #fff; border-color: var(--accent); box-shadow: none; }
        .table-dark-custom { --bs-table-bg: #1e293b; --bs-table-color: #f8fafc; border-color: #334155; }
        .imc-box { background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 15px; display: flex; align-items: center; height: 100%; }
    </style>
</head>
<body>

    <nav class="sidebar" id="sidebar">
        <div class="p-4 d-flex align-items-center border-bottom border-secondary mb-3" style="border-color: #334155 !important;">
            <i class="bi bi-activity text-primary fs-3 me-3"></i>
            <span class="brand-title fw-bold fs-5 tracking-wide">NURSELOGIC</span>
        </div>
        <ul class="nav flex-column">
            <li class="nav-item"><a class="nav-link active" onclick="cambiarVista('dashboard')"><i class="bi bi-grid-1x2"></i><span class="texto-nav">Dashboard</span></a></li>
            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('pacientes')"><i class="bi bi-people"></i><span class="texto-nav">Directorio Pacientes</span></a></li>
            <li class="nav-item"><a class="nav-link" onclick="cambiarVista('medicamentos')"><i class="bi bi-capsule"></i><span class="texto-nav">Inventario F├írmacos</span></a></li>

            <% if(isAdmin) { %>
            <li class="nav-item"><a class="nav-link text-success" onclick="cambiarVista('personal')"><i class="bi bi-shield-lock"></i><span class="texto-nav">Personal M├®dico</span></a></li>
            <% } %>

            <li class="nav-item"><a class="nav-link text-warning" onclick="cambiarVista('reportes')"><i class="bi bi-bug"></i><span class="texto-nav">Soporte T.I.</span></a></li>
            <li class="nav-item mt-5"><a class="nav-link text-danger" href="login.jsp"><i class="bi bi-box-arrow-left"></i><span class="texto-nav">Cerrar Sesi├│n</span></a></li>
        </ul>
    </nav>

    <main class="main-content" id="main-content">
        <div class="top-bar">
            <button class="btn-menu" onclick="toggleMenu()"><i class="bi bi-list"></i></button>
            <div class="text-end">
                <small class="text-secondary d-block">M├│dulo Activo</small>
                <%
                   // Seguro para que el nombre nunca se vea como "null" feo en pantalla
                   String nombreTop = (String) session.getAttribute("nombres");
                   if(nombreTop == null || nombreTop.trim().isEmpty() || nombreTop.contains("null")) {
                       nombreTop = "Usuario del Sistema";
                   }
                %>
                <span class="fw-bold"><%= nombreTop %> | <%= rolUsuario %></span>
            </div>
        </div>

        <div id="dashboard" class="vista-activa">
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="kpi-card shadow-sm" onclick="cambiarVista('pacientes')">
                        <div class="kpi-title">Pacientes</div>
                        <div class="kpi-number"><%= request.getAttribute("totalPacientes") != null ? request.getAttribute("totalPacientes") : "0" %></div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="kpi-card shadow-sm" onclick="cambiarVista('medicamentos')">
                        <div class="kpi-title">Medicamentos</div>
                        <div class="kpi-number"><%= request.getAttribute("totalMeds") != null ? request.getAttribute("totalMeds") : "0" %></div>
                    </div>
                </div>
                <% if(isAdmin) { %>
                <div class="col-md-4">
                    <div class="kpi-card shadow-sm" onclick="cambiarVista('personal')">
                        <div class="kpi-title">Personal</div>
                        <div class="kpi-number"><%= request.getAttribute("totalUsers") != null ? request.getAttribute("totalUsers") : "0" %></div>
                    </div>
                </div>
                <% } %>
            </div>

            <div class="form-section shadow-sm">
                <h5 class="text-primary mb-4 fw-bold"><i class="bi bi-file-earmark-medical me-2"></i>Nueva Admisi├│n y Triage</h5>
                <form action="registroPaciente" method="post">
                    <div class="row g-3 mb-3">
                        <div class="col-md-3"><label class="form-label small text-secondary">Nombres</label><input type="text" name="nombres" class="form-control" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">Apellidos</label><input type="text" name="apellidos" class="form-control" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">C├®dula</label><input type="text" name="cedula" class="form-control" required></div>
                        <div class="col-md-1"><label class="form-label small text-secondary">Edad</label><input type="number" name="edad" class="form-control" required></div>
                        <div class="col-md-2"><label class="form-label small text-secondary">Sexo</label><select name="sexo" class="form-select" required><option value="M">M</option><option value="F">F</option></select></div>
                    </div>

                    <div class="row g-3 mb-4">
                        <div class="col-12"><label class="form-label small text-secondary">Enfermedad Preexistente (Ej: Diabetes, Hipertensi├│n)</label><input type="text" name="enfermedad" class="form-control" placeholder="Ninguna o especificar..."></div>
                    </div>

                    <h6 class="text-secondary border-bottom border-secondary pb-2 mb-3">Evaluaci├│n Antropom├®trica (IMC)</h6>

                    <div class="row g-3 mb-4 align-items-center">
                        <div class="col-md-3"><label class="form-label small text-secondary">Estatura (m)</label><input type="number" step="0.01" id="estatura" name="estatura" class="form-control" oninput="calcularIMCTiempoReal()" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">Peso (kg)</label><input type="number" step="0.1" id="peso" name="peso" class="form-control" oninput="calcularIMCTiempoReal()" required></div>
                        <div class="col-md-6">
                            <div class="imc-box">
                                <i class="bi bi-calculator text-primary fs-3 me-3"></i>
                                <div><div class="small text-secondary">Resultado IMC</div><span id="imcValor" class="fw-bold fs-4 text-white">0.0</span><span id="imcEstado" class="badge bg-secondary ms-2">Sin datos</span></div>
                            </div>
                        </div>
                    </div>

                    <h6 class="text-secondary border-bottom border-secondary pb-2 mb-3">Signos Vitales</h6>

                    <div class="row g-3">
                        <div class="col-md-3"><label class="form-label small text-secondary">Temp (┬░C)</label><input type="number" step="0.1" name="temperatura" class="form-control" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">Presi├│n Arterial</label><input type="text" name="presion" class="form-control" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">Frec. Cardiaca (LPM)</label><input type="number" name="fc" class="form-control" required></div>
                        <div class="col-md-3"><label class="form-label small text-secondary">Saturaci├│n O2 (%)</label><input type="number" name="sat" class="form-control" required></div>
                    </div>

                    <div class="mt-4 text-end">
                        <button type="submit" class="btn btn-primary px-5 fw-bold">Guardar Historia Cl├¡nica</button>
                    </div>
                </form>
            </div>
        </div>

        <div id="pacientes" class="vista-activa d-none">
            <h3 class="mb-3">Base de Datos: Pacientes</h3>
            <div class="form-section p-0 overflow-hidden">
                <table class="table table-dark-custom table-hover m-0">
                    <thead><tr><th>Paciente</th><th>C├®dula</th><th>Edad</th></tr></thead>
                    <tbody>
                        <%
                            try {
                                Object objP = request.getAttribute("listaPacientes");
                                if(objP == null) {
                                    out.print("<tr><td colspan='3' class='text-center py-4 text-warning'>No hay datos. Entra siempre desde /dashboard</td></tr>");
                                } else if (objP instanceof List) {
                                    List<Map<String, String>> pacientes = (List<Map<String, String>>) objP;
                                    if(pacientes.isEmpty()) {
                                        out.print("<tr><td colspan='3' class='text-center py-4 text-secondary'>Sin registros cl├¡nicos.</td></tr>");
                                    } else {
                                        for(Map<String, String> p : pacientes) {
                                            out.print("<tr><td>" + p.get("nombres") + " " + p.get("apellidos") + "</td><td>" + p.get("cedula") + "</td><td>" + p.get("edad") + " a├▒os</td></tr>");
                                        }
                                    }
                                }
                            } catch(Exception e) {}
                        %>
                    </tbody>
                </table>
            </div>
        </div>

        <div id="medicamentos" class="vista-activa d-none">
            <h3 class="mb-3">Inventario Farmacol├│gico</h3>
            <div class="form-section p-0 overflow-hidden">
                <table class="table table-dark-custom table-hover m-0">
                    <thead><tr><th>Medicamento</th><th>Stock Disponible</th></tr></thead>
                    <tbody>
                        <tr><td colspan="2" class="text-center py-4 text-secondary">Bodega vac├¡a.</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div id="personal" class="vista-activa d-none">
            <h3 class="mb-3">Gesti├│n de Personal M├®dico Registrado</h3>
            <div class="form-section p-0 overflow-hidden">
                <table class="table table-dark-custom table-hover m-0">
                    <thead><tr><th>Nombres Completos</th><th>Correo</th><th>Rol Asignado</th></tr></thead>
                    <tbody>
                        <%
                            try {
                                Object objU = request.getAttribute("listaUsuarios");
                                if(objU == null) {
                                    out.print("<tr><td colspan='3' class='text-center py-4 text-warning'>No hay datos. Entra siempre desde /dashboard</td></tr>");
                                } else if (objU instanceof List) {
                                    List<Map<String, String>> usuarios = (List<Map<String, String>>) objU;
                                    if(usuarios.isEmpty()) {
                                        out.print("<tr><td colspan='3' class='text-center py-4 text-secondary'>No hay personal registrado.</td></tr>");
                                    } else {
                                        for(Map<String, String> u : usuarios) {
                                            String r = u.get("rol");
                                            String badge = "Admin".equalsIgnoreCase(r) ? "bg-success" : ("Pendiente".equalsIgnoreCase(r) ? "bg-warning text-dark" : "bg-primary");
                                            out.print("<tr><td>" + u.get("nombres") + " " + u.get("apellidos") + "</td><td>" + u.get("correo") + "</td><td><span class='badge " + badge + "'>" + r + "</span></td></tr>");
                                        }
                                    }
                                }
                            } catch(Exception e) {}
                        %>
                    </tbody>
                </table>
            </div>
        </div>

        <div id="reportes" class="vista-activa d-none">
            <h3 class="mb-4">Soporte T├®cnico</h3>
            <div class="form-section text-center">
                <p class="mb-4">┬┐Encontraste un error en el sistema? Graba tu pantalla y mu├®stranos qu├® sucede.</p>
                <button id="btnGrabar" class="btn btn-danger px-4" onclick="iniciarGrabacion()"><i class="bi bi-record-circle me-2"></i>Iniciar Grabaci├│n</button>
                <button id="btnDetener" class="btn btn-secondary px-4 d-none" onclick="detenerGrabacion()"><i class="bi bi-stop-circle me-2"></i>Detener Grabaci├│n</button>
                <video id="videoPreview" controls class="mt-4 w-100 d-none rounded" style="border: 1px solid #334155; background: #0f172a; max-height: 400px;"></video>
            </div>
        </div>

    </main>

    <script>
        function toggleMenu() {
            document.getElementById('sidebar').classList.toggle('contraida');
            document.getElementById('main-content').classList.toggle('expandida');
        }

        function cambiarVista(id) {
            document.querySelectorAll('.vista-activa').forEach(el => el.classList.add('d-none'));
            document.getElementById(id).classList.remove('d-none');
            document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));
            event.currentTarget.classList.add('active');
        }

        function calcularIMCTiempoReal() {
            let p = parseFloat(document.getElementById('peso').value);
            let a = parseFloat(document.getElementById('estatura').value);
            let val = document.getElementById('imcValor');
            let est = document.getElementById('imcEstado');

            if(p > 0 && a > 0) {
                let imc = p / (a * a);
                val.innerText = imc.toFixed(1);
                est.classList.remove('bg-secondary', 'bg-warning', 'bg-success', 'bg-danger');

                if(imc < 18.5) { est.innerText = 'Bajo Peso'; est.classList.add('bg-warning'); }
                else if(imc < 25) { est.innerText = 'Normal'; est.classList.add('bg-success'); }
                else { est.innerText = 'Sobrepeso/Obesidad'; est.classList.add('bg-danger'); }
            } else {
                val.innerText = '0.0';
                est.innerText = 'Sin datos';
                est.className = 'badge bg-secondary ms-2';
            }
        }

        let grabador;
        let fragmentos = [];
        async function iniciarGrabacion() {
            try {
                const stream = await navigator.mediaDevices.getDisplayMedia({ video: true });
                grabador = new MediaRecorder(stream);
                grabador.ondataavailable = (e) => { if (e.data.size > 0) fragmentos.push(e.data); };
                grabador.onstop = () => {
                    document.getElementById('videoPreview').src = URL.createObjectURL(new Blob(fragmentos, { type: 'video/webm' }));
                    document.getElementById('videoPreview').classList.remove('d-none');
                    fragmentos = [];
                };
                grabador.start();
                document.getElementById('btnGrabar').classList.add('d-none');
                document.getElementById('btnDetener').classList.remove('d-none');
                stream.getVideoTracks()[0].onended = () => detenerGrabacion();
            } catch(err) { console.error("Error al grabar: ", err); }
        }

        function detenerGrabacion() {
            if(grabador && grabador.state !== "inactive") { grabador.stop(); grabador.stream.getTracks().forEach(t => t.stop()); }
            document.getElementById('btnGrabar').classList.remove('d-none');
            document.getElementById('btnDetener').classList.add('d-none');
        }
    </script>
</body>
</html>
