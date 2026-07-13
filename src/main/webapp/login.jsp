<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>NURSELOGIC - Acceso Seguro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #0f172a; color: #fff; font-family: 'Segoe UI', Roboto, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; margin: 0; }

        .login-container { background: #1e293b; padding: 3rem; border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); width: 100%; max-width: 420px; z-index: 10; position: relative; border: 1px solid #334155; }
        .form-control { background: #0f172a; border: 1px solid #334155; color: #f8fafc; border-radius: 6px; padding: 12px; }
        .form-control:focus { background: #0f172a; color: #fff; border-color: #3b82f6; box-shadow: 0 0 0 0.2rem rgba(59, 130, 246, 0.25); }
        .form-control::placeholder { color: #64748b; }
        .btn-primary { background: #2563eb; border: none; padding: 12px; font-weight: 600; letter-spacing: 1px; width: 100%; margin-top: 10px; }
        .btn-primary:hover { background: #1d4ed8; }
        .btn-success { background: #10b981; border: none; padding: 12px; font-weight: 600; width: 100%; margin-top: 10px; }

        /* Animación Pulso Cardiaco */
        .heartbeat-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 0; opacity: 0.15; pointer-events: none; }
        .heartbeat-line { stroke-dasharray: 2000; stroke-dashoffset: 2000; animation: dash 3.5s linear infinite; }
        @keyframes dash { to { stroke-dashoffset: 0; } }
    </style>
</head>
<body>

    <svg class="heartbeat-bg" viewBox="0 0 1000 200" preserveAspectRatio="none">
        <path class="heartbeat-line" d="M0,100 L300,100 L330,50 L360,150 L390,20 L420,180 L450,100 L1000,100" fill="none" stroke="#3b82f6" stroke-width="4"></path>
    </svg>

    <div class="login-container">
        <h3 class="text-center fw-bold mb-1" style="color: #3b82f6; letter-spacing: 2px;">NURSELOGIC</h3>
        <p class="text-center mb-4" style="color: #94a3b8; font-size: 0.85rem;">SISTEMA CLÍNICO INTEGRADO</p>

        <% if(request.getAttribute("error") != null) { %>
            <div class="alert alert-warning p-2 text-center small"><%= request.getAttribute("error") %></div>
        <% } %>

        <div id="panel-login">
            <form action="login" method="post">
                <div class="mb-3">
                    <label class="form-label small text-secondary">Correo Electrónico</label>
                    <input type="text" name="usuario" class="form-control" required>
                </div>
                <div class="mb-4">
                    <label class="form-label small text-secondary">Contraseña</label>
                    <input type="password" name="clave" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary">AUTENTICAR</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small" style="color: #94a3b8;" onclick="togglePanels()">¿Personal nuevo? Solicitar registro</a>
            </div>
        </div>

        <div id="panel-register" class="d-none">
            <form action="registroUsuario" method="post">
                <div class="row g-2 mb-3">
                    <div class="col-6"><input type="text" name="nombres" class="form-control form-control-sm" placeholder="Nombres" required></div>
                    <div class="col-6"><input type="text" name="apellidos" class="form-control form-control-sm" placeholder="Apellidos" required></div>
                    <div class="col-12"><input type="email" name="correo" class="form-control form-control-sm" placeholder="Correo" required></div>
                    <div class="col-6"><input type="text" name="cedula" class="form-control form-control-sm" placeholder="Cédula" required></div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control form-control-sm" placeholder="Teléfono" required></div>
                    <div class="col-12"><input type="text" name="direccion" class="form-control form-control-sm" placeholder="Dirección" required></div>
                    <div class="col-12"><input type="password" name="clave" class="form-control form-control-sm" placeholder="Crear Contraseña" required></div>
                </div>
                <button type="submit" class="btn btn-success">REGISTRAR USUARIO</button>
            </form>
            <div class="text-center mt-3">
                <a href="#" class="text-decoration-none small" style="color: #94a3b8;" onclick="togglePanels()">Volver al Login</a>
            </div>
        </div>
    </div>

    <script>
        function togglePanels() {
            document.getElementById('panel-login').classList.toggle('d-none');
            document.getElementById('panel-register').classList.toggle('d-none');
        }
    </script>
</body>
</html>