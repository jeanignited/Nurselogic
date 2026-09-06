<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>NURSELOGIC - Acceso Seguro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-main: #0b0f19;
            --accent: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.5);
            --glass-bg: rgba(30, 41, 59, 0.6);
            --glass-border: 1px solid rgba(255, 255, 255, 0.1);
        }
        body { 
            background-color: var(--bg-main); 
            background-image: radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.05), transparent 60%);
            color: #fff; 
            font-family: 'Inter', sans-serif; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            overflow: hidden; 
            margin: 0; 
        }
        .login-container { 
            background: var(--glass-bg); 
            backdrop-filter: blur(16px);
            padding: 3.5rem 3rem; 
            border-radius: 20px; 
            box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.05); 
            width: 100%; 
            max-width: 450px; 
            z-index: 10; 
            position: relative; 
            border: var(--glass-border); 
            transition: all 0.4s ease;
        }
        .form-control, .form-select { 
            background: rgba(15, 23, 42, 0.6); 
            border: var(--glass-border); 
            color: #f8fafc; 
            border-radius: 8px; 
            padding: 12px 15px; 
            font-size: 0.95rem;
            transition: 0.3s;
        }
        .form-control:focus, .form-select:focus { 
            background: rgba(15, 23, 42, 0.9); 
            color: #fff; 
            border-color: var(--accent); 
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15); 
        }
        .form-control::placeholder { color: #64748b; }
        .btn-primary { 
            background: linear-gradient(135deg, #3b82f6, #2563eb); 
            border: none; 
            padding: 14px; 
            font-weight: 600; 
            letter-spacing: 1px; 
            width: 100%; 
            margin-top: 15px; 
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
            transition: 0.3s;
        }
        .btn-primary:hover { 
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.5);
        }
        .btn-success { background: linear-gradient(135deg, #10b981, #059669); border: none; padding: 14px; font-weight: 600; width: 100%; margin-top: 15px; border-radius: 8px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3); transition: 0.3s;}
        .btn-success:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5); }
        .heartbeat-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 0; opacity: 0.2; pointer-events: none; }
        .heartbeat-line { stroke-dasharray: 2000; stroke-dashoffset: 2000; animation: dash 4s cubic-bezier(0.4, 0, 0.2, 1) infinite; filter: drop-shadow(0 0 8px var(--accent)); }
        @keyframes dash { to { stroke-dashoffset: 0; } }
        .panel { transition: opacity 0.3s ease; }
        .alert { backdrop-filter: blur(5px); border: none; }
        /* Dropdown Estilos General (Modo Oscuro) */
        .dropdown-menu { background: #0f172a !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; }
        .dropdown-item { color: #f8fafc !important; }
        .dropdown-item:hover, .dropdown-item:focus { background: rgba(59, 130, 246, 0.3) !important; color: #ffffff !important; }
        /* Modo Claro Overrides */
        html[data-theme="light"] {
            --bg-main: #f0f4f8;
            --accent: #2563eb;
            --accent-glow: rgba(37, 99, 235, 0.3);
            --glass-bg: rgba(255, 255, 255, 0.85);
            --glass-border: 1px solid rgba(0, 0, 0, 0.1);
        }
        html[data-theme="light"] body {
            background-color: var(--bg-main);
            background-image: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.08), transparent 60%);
            color: #1e293b;
        }
        html[data-theme="light"] .heartbeat-bg { opacity: 1.0 !important; }
        html[data-theme="light"] .heartbeat-line { stroke: #0284c7 !important; stroke-width: 5 !important; filter: drop-shadow(0 0 12px rgba(2, 132, 199, 0.6)) !important; }
        html[data-theme="light"] .dropdown-menu { background: rgba(255, 255, 255, 0.95) !important; border: 1px solid rgba(0, 0, 0, 0.15) !important; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important; }
        html[data-theme="light"] .dropdown-item { color: #1e293b !important; }
        html[data-theme="light"] .dropdown-item:hover, html[data-theme="light"] .dropdown-item:focus { background: rgba(37, 99, 235, 0.1) !important; color: #1d4ed8 !important; }
        html[data-theme="light"] .login-container, html[data-theme="light"] .register-container {
            background: var(--glass-bg);
            border-color: rgba(0, 0, 0, 0.1);
            color: #1e293b;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
        }
        html[data-theme="light"] .text-white, html[data-theme="light"] .text-light, html[data-theme="light"] h3, html[data-theme="light"] h4, html[data-theme="light"] h5 {
            color: #1e293b !important;
        }
        html[data-theme="light"] .text-secondary {
            color: #64748b !important;
        }
        html[data-theme="light"] .form-control, html[data-theme="light"] .form-select {
            background: rgba(255, 255, 255, 0.9);
            border-color: rgba(0, 0, 0, 0.2);
            color: #1e293b;
        }
        html[data-theme="light"] .form-control:focus, html[data-theme="light"] .form-select:focus {
            background: #ffffff;
            color: #0f172a;
            border-color: #2563eb;
        }
        html[data-theme="light"] .nav-tabs .nav-link {
            color: #64748b;
        }
        html[data-theme="light"] .nav-tabs .nav-link.active {
            color: #2563eb !important;
            border-color: #2563eb !important;
            background: rgba(37, 99, 235, 0.05);
        }
    </style>
</head>
<body>
    <script>
        (function() {
            let saved = localStorage.getItem('nurselogic_theme') || 'auto';
            let actual = saved === 'auto' ? (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark') : saved;
            document.documentElement.setAttribute('data-theme', actual);
        })();
    </script>
    <!-- Widget Selector de Tema -->
    <div class="position-fixed top-0 end-0 p-3" style="z-index: 9999;">
        <div class="dropdown">
            <button class="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-2 px-3 py-2 rounded-pill shadow-sm" type="button" id="themeDropdownLogin" data-bs-toggle="dropdown" aria-expanded="false" style="background: var(--glass-bg); backdrop-filter: blur(10px); border: var(--glass-border); color: inherit;">
                <i class="bi bi-moon-stars-fill" id="themeIconLogin"></i>
                <span id="themeLabelLogin" class="small fw-semibold">Oscuro</span>
            </button>
            <ul class="dropdown-menu dropdown-menu-end shadow-lg rounded-3 border-0" aria-labelledby="themeDropdownLogin" style="background: var(--glass-bg); backdrop-filter: blur(15px); border: var(--glass-border);">
                <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('dark'); return false;"><i class="bi bi-moon-stars-fill text-primary"></i> Modo Oscuro</a></li>
                <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('light'); return false;"><i class="bi bi-sun-fill text-warning"></i> Modo Claro</a></li>
                <li><hr class="dropdown-divider border-secondary opacity-25"></li>
                <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#" onclick="setTheme('auto'); return false;"><i class="bi bi-display text-info"></i> Sistema (Auto)</a></li>
            </ul>
        </div>
    </div>

    <svg class="heartbeat-bg" viewBox="0 0 1000 200" preserveAspectRatio="none">
        <path class="heartbeat-line" d="M0,100 L300,100 L330,50 L360,150 L390,20 L420,180 L450,100 L1000,100" fill="none" stroke="#3b82f6" stroke-width="3"></path>
    </svg>

    <div class="login-container">
        <div class="text-center mb-4">
            <i class="bi bi-activity text-primary" style="font-size: 2.5rem; filter: drop-shadow(0 0 10px var(--accent));"></i>
            <h3 class="fw-bold mt-2 mb-1" style="color: #fff; letter-spacing: 2px;">NURSELOGIC</h3>
            <p style="color: #94a3b8; font-size: 0.85rem; letter-spacing: 1px;">SISTEMA CLÍNICO INTEGRADO</p>
        </div>

        <% if(request.getAttribute("error") != null) { %>
            <div class="alert alert-danger p-3 text-center small rounded-3" style="background: rgba(239, 68, 68, 0.15); color: #fca5a5;"><i class="bi bi-exclamation-triangle me-2"></i><%= request.getAttribute("error") %></div>
        <% } %>
        <% if(request.getAttribute("mensaje") != null) { %>
            <div class="alert alert-success p-3 text-center small rounded-3" style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7;"><i class="bi bi-check-circle me-2"></i><%= request.getAttribute("mensaje") %></div>
        <% } %>

        <% 
           boolean showRecover = request.getAttribute("showRecover") != null && (Boolean)request.getAttribute("showRecover");
           boolean showReset = request.getAttribute("showReset") != null && (Boolean)request.getAttribute("showReset");
           boolean showLogin = !showRecover && !showReset;
        %>

        <!-- PANEL LOGIN -->
        <div id="panel-login" class="panel <%= showLogin ? "" : "d-none" %>">
            <form action="login" method="post">
                <div class="mb-3">
                    <label class="form-label small text-secondary fw-semibold">Correo Electrónico</label>
                    <input type="email" name="usuario" class="form-control" placeholder="usuario@ejemplo.com" required>
                </div>
                <div class="mb-4">
                    <div class="d-flex justify-content-between">
                        <label class="form-label small text-secondary fw-semibold">Contraseña</label>
                        <a href="#" class="small text-decoration-none" style="color: var(--accent);" onclick="mostrarPanel('panel-recover')">¿Olvidaste tu clave?</a>
                    </div>
                    <input type="password" name="clave" class="form-control" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary"><i class="bi bi-box-arrow-in-right me-2"></i>AUTENTICAR</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small text-secondary" onclick="mostrarPanel('panel-register')">¿Personal nuevo o Paciente? <span class="text-white">Solicitar registro</span></a>
            </div>
        </div>

        <!-- PANEL REGISTRO -->
        <div id="panel-register" class="panel d-none">
            <form action="registroUsuario" method="post">
                <div class="row g-2 mb-3">
                    <div class="col-6"><input type="text" name="nombres" class="form-control" placeholder="Nombres" required></div>
                    <div class="col-6"><input type="text" name="apellidos" class="form-control" placeholder="Apellidos" required></div>
                    <div class="col-12"><input type="email" name="correo" class="form-control" placeholder="Correo Electrónico" required></div>
                    <div class="col-6"><input type="text" name="cedula" class="form-control" placeholder="Cédula (10 dígitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required></div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control" placeholder="Teléfono (10 dígitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required></div>
                    <div class="col-12"><input type="text" name="direccion" class="form-control" placeholder="Dirección" required></div>
                    <div class="col-12"><input type="password" name="clave" class="form-control" placeholder="Crear Contraseña" required></div>
                    <div class="col-12">
                        <select name="tipoUsuario" class="form-select" required>
                            <option value="" disabled selected>Seleccione el tipo de cuenta...</option>
                            <option value="Paciente">Soy Paciente</option>
                            <option value="Medico">Soy Personal Médico</option>
                        </select>
                    </div>
                </div>
                <button type="submit" class="btn btn-success"><i class="bi bi-person-plus me-2"></i>REGISTRAR USUARIO</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small text-secondary" onclick="mostrarPanel('panel-login')"><i class="bi bi-arrow-left me-1"></i>Volver al Login</a>
            </div>
        </div>

        <!-- PANEL RECUPERAR CONTRASEÑA -->
        <div id="panel-recover" class="panel <%= showRecover ? "" : "d-none" %>">
            <p class="text-center text-secondary small mb-4">Ingresa tu correo registrado para enviarte un código de verificación y desbloquear tu cuenta.</p>
            <form action="recuperar" method="post">
                <input type="hidden" name="action" value="enviarCodigo">
                <div class="mb-4">
                    <label class="form-label small text-secondary fw-semibold">Correo Electrónico</label>
                    <input type="email" name="correo" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary"><i class="bi bi-envelope-paper me-2"></i>ENVIAR CÓDIGO</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small text-secondary" onclick="mostrarPanel('panel-login')"><i class="bi bi-arrow-left me-1"></i>Volver al Login</a>
            </div>
        </div>

        <!-- PANEL RESETEAR CLAVE (Ingresar código) -->
        <div id="panel-reset" class="panel <%= showReset ? "" : "d-none" %>">
            <p class="text-center text-secondary small mb-4">Ingresa el código de 6 dígitos que enviamos a tu correo para crear una nueva contraseña.</p>
            <form action="recuperar" method="post">
                <input type="hidden" name="action" value="resetClave">
                <input type="hidden" name="correo" value="<%= request.getAttribute("correoRecuperacion") != null ? request.getAttribute("correoRecuperacion") : "" %>">
                <div class="mb-3">
                    <label class="form-label small text-secondary fw-semibold">Código de Verificación</label>
                    <input type="text" name="codigo" class="form-control text-center fs-4 letter-spacing-2" placeholder="000000" maxlength="6" pattern="\d{6}" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required>
                </div>
                <div class="mb-4">
                    <label class="form-label small text-secondary fw-semibold">Nueva Contraseña</label>
                    <input type="password" name="nuevaClave" class="form-control" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-success"><i class="bi bi-key me-2"></i>ACTUALIZAR CONTRASEÑA</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small text-secondary" onclick="mostrarPanel('panel-login')"><i class="bi bi-arrow-left me-1"></i>Volver al Login</a>
            </div>
        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function mostrarPanel(idPanel) {
            document.querySelectorAll('.panel').forEach(el => el.classList.add('d-none'));
            document.getElementById(idPanel).classList.remove('d-none');
        }

        function setTheme(theme) {
            localStorage.setItem('nurselogic_theme', theme);
            applyTheme(theme);
        }

        function applyTheme(theme) {
            let actualTheme = theme;
            if (theme === 'auto') {
                actualTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            }
            document.documentElement.setAttribute('data-theme', actualTheme);

            let iconLogin = document.getElementById('themeIconLogin');
            let labelLogin = document.getElementById('themeLabelLogin');
            let iconClass = 'bi-moon-stars-fill';
            let labelText = 'Oscuro';
            if (theme === 'light') { iconClass = 'bi-sun-fill'; labelText = 'Claro'; }
            else if (theme === 'auto') { iconClass = 'bi-display'; labelText = 'Auto'; }

            if (iconLogin) iconLogin.className = 'bi ' + iconClass;
            if (labelLogin) labelLogin.innerText = labelText;
        }

        (function() {
            let savedTheme = localStorage.getItem('nurselogic_theme') || 'auto';
            applyTheme(savedTheme);
            window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', e => {
                if (localStorage.getItem('nurselogic_theme') === 'auto') {
                    applyTheme('auto');
                }
            });
        })();
    </script>
</body>
</html>
