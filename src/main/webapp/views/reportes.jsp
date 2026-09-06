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
%>        <div id="reportes" class="vista-activa d-none">

            <div class="form-section text-center max-w-md mx-auto" style="max-width: 600px;">

                <div class="mb-4">

                    <i class="bi bi-headset text-primary" style="font-size: 4rem; filter: drop-shadow(0 0 15px var(--accent));"></i>

                </div>

                <h3 class="mb-3 fw-bold text-theme">Soporte Técnico Especializado</h3>

                <p class="mb-5 text-secondary fs-5">¿Encontraste un error en el sistema? Graba tu pantalla y envíanos el video para que nuestro equipo lo resuelva rápidamente.</p>

                <button id="btnGrabar" class="btn btn-danger px-5 py-3 fs-5 rounded-pill shadow-lg" onclick="iniciarGrabacion()"><i class="bi bi-record-circle me-2"></i>Iniciar Grabación</button>

                <button id="btnDetener" class="btn btn-secondary px-5 py-3 fs-5 rounded-pill d-none shadow-lg" onclick="detenerGrabacion()"><i class="bi bi-stop-circle me-2 text-danger"></i>Detener Grabación</button>

                

                <div class="mt-5 p-2 bg-dark rounded-4" style="border: var(--glass-border);">

                    <video id="videoPreview" controls class="w-100 rounded-3 d-none bg-black" style="max-height: 400px;"></video>

                    <div id="videoPlaceholder" class="py-5 text-secondary"><i class="bi bi-camera-video me-2"></i>La vista previa aparecerá aquí</div>

                </div>

            </div>

        </div>








