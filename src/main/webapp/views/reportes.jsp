<%@ page pageEncoding="UTF-8" %>
<%@ page import="java.util.List,java.util.Map" %>
<%@ page import="com.nurselogic.model.*" %>
<%@ page import="com.nurselogic.config.JPAUtil" %>
<%@ page import="jakarta.persistence.EntityManager" %>
<%
    boolean isAdmin = Boolean.TRUE.equals(request.getAttribute("isAdmin"));
    boolean permSoporteTI = Boolean.TRUE.equals(request.getAttribute("permSoporteTI"));
%>

<div id="reportes" class="vista-activa d-none">
    <% if (isAdmin) { %>
        <!-- PANEL DE SOPORTE T.I. PARA ADMINISTRADORES -->
        <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
            <div>
                <h2 class="fw-bold text-theme m-0"><i class="bi bi-display me-2 text-primary"></i>Panel de Control T.I.</h2>
                <p class="text-secondary mt-1 mb-0">Sistema de Ticketing y Visualización de Reportes (Vista estilo cámaras de seguridad)</p>
            </div>
            <div class="d-flex gap-2">
                <select id="filtroNivelTI" class="form-select form-select-sm bg-dark text-white border-secondary" onchange="filtrarTicketsTI()">
                    <option value="todos">Todos los niveles</option>
                    <option value="leve">Leve</option>
                    <option value="moderado">Moderado</option>
                    <option value="critico">Crítico</option>
                </select>
                <button class="btn btn-outline-info rounded-pill px-4" onclick="location.reload()"><i class="bi bi-arrow-clockwise me-2"></i>Actualizar Panel</button>
            </div>
        </div>

        <div class="row g-4" id="contenedorTicketsTI">
            <%
                try {
                    EntityManager em = JPAUtil.getEntityManager();
                    em.getTransaction().begin();
                    em.createNativeQuery("CREATE TABLE IF NOT EXISTS tickets_soporte (" +
                            "id INT AUTO_INCREMENT PRIMARY KEY, " +
                            "titulo VARCHAR(255), " +
                            "descripcion TEXT, " +
                            "nivel_alerta VARCHAR(50), " +
                            "ruta_video VARCHAR(255), " +
                            "fecha_reporte DATETIME, " +
                            "estado VARCHAR(50) DEFAULT 'Pendiente')").executeUpdate();
                    em.getTransaction().commit();

                    List<Object[]> tickets = em.createNativeQuery(
                        "SELECT id, titulo, descripcion, nivel_alerta, ruta_video, fecha_reporte, estado FROM tickets_soporte ORDER BY id DESC"
                    ).getResultList();
                    em.close();

                    if (tickets.isEmpty()) {
            %>
                        <div class="col-12 text-center py-5">
                            <i class="bi bi-check-circle text-success" style="font-size: 3rem;"></i>
                            <h4 class="mt-3 text-secondary">No hay reportes de soporte pendientes</h4>
                        </div>
            <%
                    } else {
                        for (Object[] t : tickets) {
                            int id = (Integer) t[0];
                            String titulo = (String) t[1];
                            String descripcion = (String) t[2];
                            String alerta = (String) t[3];
                            String rutaVideo = (String) t[4];
                            String fecha = t[5].toString();
                            String estado = (String) t[6];

                            String badgeClass = "bg-secondary";
                            if ("Leve".equalsIgnoreCase(alerta)) badgeClass = "bg-info text-dark";
                            else if ("Moderado".equalsIgnoreCase(alerta)) badgeClass = "bg-warning text-dark";
                            else if ("Crítico".equalsIgnoreCase(alerta) || "Critico".equalsIgnoreCase(alerta)) badgeClass = "bg-danger text-white";

                            boolean esResuelto = "Resuelto".equalsIgnoreCase(estado);
            %>
            <div class="col-md-6 col-lg-4 ticket-card" data-nivel="<%= alerta.toLowerCase() %>">
                <div class="card h-100 bg-dark text-white" style="border: var(--glass-border); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
                    <div class="card-header border-0 d-flex justify-content-between align-items-center" style="background: rgba(255,255,255,0.05);">
                        <span class="badge <%= badgeClass %>"><i class="bi bi-exclamation-triangle-fill me-1"></i><%= alerta %></span>
                        <span class="small text-secondary"><i class="bi bi-clock me-1"></i><%= fecha.substring(0,16) %></span>
                    </div>
                    
                    <div class="video-container" style="background: #000; position: relative;">
                        <% if (rutaVideo != null && !rutaVideo.isEmpty()) { %>
                            <video src="<%= rutaVideo %>" controls class="w-100" style="max-height: 200px; object-fit: contain;"></video>
                        <% } else { %>
                            <div class="d-flex justify-content-center align-items-center" style="height: 200px; color: #444;">
                                <i class="bi bi-camera-video-off" style="font-size: 2rem;"></i>
                            </div>
                        <% } %>
                        <div style="position: absolute; top: 10px; right: 10px;">
                            <span class="badge <%= esResuelto ? "bg-success" : "bg-danger" %> px-2 py-1"><i class="bi bi-record-circle me-1"></i><%= esResuelto ? "RESUELTO" : "REC" %></span>
                        </div>
                    </div>

                    <div class="card-body">
                        <h5 class="card-title fw-bold text-truncate" title="<%= titulo %>"><%= titulo %></h5>
                        <p class="card-text small text-secondary" style="max-height: 80px; overflow-y: auto; padding-right: 5px; white-space: pre-wrap; cursor: pointer;" title="Haz clic para expandir o contraer" onclick="this.style.maxHeight = this.style.maxHeight === '80px' ? 'none' : '80px';"><%= descripcion %></p>
                    </div>

                    <div class="card-footer border-0 bg-transparent text-end">
                        <% if (!esResuelto) { %>
                            <form action="soporteAction" method="POST">
                                <input type="hidden" name="action" value="resolver">
                                <input type="hidden" name="id" value="<%= id %>">
                                <button type="submit" class="btn btn-sm btn-outline-success rounded-pill px-3"><i class="bi bi-check2-all me-1"></i>Marcar Resuelto</button>
                            </form>
                        <% } else { %>
                            <span class="text-success small fw-bold"><i class="bi bi-check-circle-fill me-1"></i>Ticket Cerrado</span>
                        <% } %>
                    </div>
                </div>
            </div>
            <%
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
            %>
                <div class="alert alert-danger w-100">Error al cargar tickets de soporte: <%= e.getMessage() %></div>
            <%  } %>
        </div>

    <% } else { %>
        <!-- FORMULARIO DE SOPORTE PARA USUARIOS NORMALES -->
        <div class="form-section max-w-md mx-auto" style="max-width: 800px;">
            <div class="text-center mb-4">
                <i class="bi bi-headset text-primary" style="font-size: 3rem; filter: drop-shadow(0 0 15px var(--accent));"></i>
                <h3 class="mt-3 fw-bold text-theme">Reportar Error en el Sistema</h3>
                <p class="text-secondary">Graba tu pantalla mostrando el error y describe el problema para que el equipo T.I. pueda ayudarte.</p>
            </div>

            <form id="formSoporteTicket" onsubmit="enviarTicketSoporte(event)">
                <div class="row g-3 mb-4 text-start">
                    <div class="col-md-8">
                        <label class="form-label small text-secondary fw-semibold">Título del Problema</label>
                        <input type="text" id="ticketTitulo" class="form-control" placeholder="Ej: No puedo agendar una cita" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label small text-secondary fw-semibold">Nivel de Alerta</label>
                        <select id="ticketAlerta" class="form-select" required>
                            <option value="Leve" class="text-info">🔵 Leve (Estético/Menor)</option>
                            <option value="Moderado" class="text-warning">🟡 Moderado (Funcionalidad afectada)</option>
                            <option value="Crítico" class="text-danger fw-bold">🔴 Crítico (Bloquea el trabajo)</option>
                        </select>
                    </div>
                    <div class="col-12">
                        <label class="form-label small text-secondary fw-semibold">Descripción Detallada</label>
                        <textarea id="ticketDesc" class="form-control" rows="3" placeholder="Explica los pasos que seguiste antes del error..." required></textarea>
                    </div>
                </div>

                <!-- Controles de Grabación -->
                <div class="p-4 bg-dark rounded-4 mb-4 text-center" style="border: var(--glass-border); position: relative;">
                    <div id="estadoGrabacion" class="mb-3">
                        <span class="badge bg-secondary p-2 fs-6"><i class="bi bi-camera-video me-2"></i>Video Evidencia (Obligatorio)</span>
                    </div>

                    <video id="soporteVideoPreview" controls class="w-100 rounded-3 d-none bg-black mb-3" style="max-height: 400px;"></video>
                    
                    <button type="button" id="btnGrabarSoporte" class="btn btn-danger px-4 py-2 rounded-pill shadow-lg me-2" onclick="iniciarGrabacionSoporte()">
                        <i class="bi bi-record-circle me-2"></i>Grabar Pantalla
                    </button>
                    <button type="button" id="btnDetenerSoporte" class="btn btn-secondary px-4 py-2 rounded-pill d-none shadow-lg me-2" onclick="detenerGrabacionSoporte()">
                        <i class="bi bi-stop-circle me-2 text-danger"></i>Detener Grabación
                    </button>
                </div>

                <div class="text-center">
                    <button type="submit" id="btnEnviarTicket" class="btn btn-primary px-5 py-3 fs-5 rounded-pill shadow-lg w-100" disabled>
                        <i class="bi bi-send-fill me-2"></i>Enviar Ticket a Soporte T.I.
                    </button>
                </div>
            </form>
        </div>

        <script>
            let soporteGrabador;
            let soporteFragmentos = [];
            let soporteBlob = null;

            async function iniciarGrabacionSoporte() {
                try {
                    const stream = await navigator.mediaDevices.getDisplayMedia({ 
                        video: {
                            displaySurface: "browser"
                        },
                        audio: false,
                        preferCurrentTab: true
                    });
                    
                    soporteGrabador = new MediaRecorder(stream);
                    soporteFragmentos = [];

                    soporteGrabador.ondataavailable = (e) => { 
                        if (e.data.size > 0) soporteFragmentos.push(e.data); 
                    };

                    soporteGrabador.onstop = () => {
                        soporteBlob = new Blob(soporteFragmentos, { type: 'video/webm' });
                        const videoUrl = URL.createObjectURL(soporteBlob);
                        
                        const videoEl = document.getElementById('soporteVideoPreview');
                        videoEl.src = videoUrl;
                        videoEl.classList.remove('d-none');
                        
                        document.getElementById('estadoGrabacion').innerHTML = '<span class="badge bg-success p-2 fs-6"><i class="bi bi-check-circle me-2"></i>Grabación Finalizada</span>';
                        document.getElementById('btnEnviarTicket').disabled = false;
                        document.getElementById('btnEnviarTicket').classList.add('btn-success');
                        document.getElementById('btnEnviarTicket').classList.remove('btn-primary');
                    };

                    soporteGrabador.start();
                    
                    document.getElementById('btnGrabarSoporte').classList.add('d-none');
                    document.getElementById('btnDetenerSoporte').classList.remove('d-none');
                    document.getElementById('estadoGrabacion').innerHTML = '<span class="badge bg-danger p-2 fs-6 blink"><i class="bi bi-record-circle me-2"></i>Grabando...</span>';
                    
                } catch (err) {
                    console.error("Error al compartir pantalla: ", err);
                    alert("Debes permitir compartir pantalla para reportar el error.");
                }
            }

            function detenerGrabacionSoporte() {
                if(soporteGrabador && soporteGrabador.state !== "inactive") { 
                    soporteGrabador.stop(); 
                    soporteGrabador.stream.getTracks().forEach(t => t.stop()); 
                }
                document.getElementById('btnGrabarSoporte').classList.add('d-none');
                document.getElementById('btnDetenerSoporte').classList.add('d-none');
            }

            function enviarTicketSoporte(e) {
                e.preventDefault();
                
                if (!soporteBlob) {
                    alert("Por favor, graba la pantalla mostrando el error antes de enviar.");
                    return;
                }

                const titulo = document.getElementById('ticketTitulo').value;
                const desc = document.getElementById('ticketDesc').value;
                const alerta = document.getElementById('ticketAlerta').value;
                const btn = document.getElementById('btnEnviarTicket');
                
                btn.disabled = true;
                btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Enviando...';

                const formData = new FormData();
                formData.append('titulo', titulo);
                formData.append('descripcion', desc);
                formData.append('nivelAlerta', alerta);
                formData.append('video', soporteBlob, 'grabacion.webm');

                fetch('soporteAction', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if(data.success) {
                        alert(data.message);
                        // Resetear formulario
                        document.getElementById('formSoporteTicket').reset();
                        document.getElementById('soporteVideoPreview').classList.add('d-none');
                        document.getElementById('soporteVideoPreview').src = "";
                        soporteBlob = null;
                        document.getElementById('btnGrabarSoporte').classList.remove('d-none');
                        document.getElementById('estadoGrabacion').innerHTML = '<span class="badge bg-secondary p-2 fs-6"><i class="bi bi-camera-video me-2"></i>Video Evidencia (Obligatorio)</span>';
                        btn.innerHTML = '<i class="bi bi-send-fill me-2"></i>Enviar Ticket a Soporte T.I.';
                        btn.classList.add('btn-primary');
                        btn.classList.remove('btn-success');
                        btn.disabled = true;
                    } else {
                        alert("Error: " + data.message);
                        btn.disabled = false;
                        btn.innerHTML = '<i class="bi bi-send-fill me-2"></i>Intentar de Nuevo';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error de red al enviar el ticket.');
                    btn.disabled = false;
                    btn.innerHTML = '<i class="bi bi-send-fill me-2"></i>Intentar de Nuevo';
                });
            }
        </script>
        
        <style>
            .blink { animation: blinker 1.5s linear infinite; }
            @keyframes blinker { 50% { opacity: 0; } }
        </style>
    <% } %>
</div>
