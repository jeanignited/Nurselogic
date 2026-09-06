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
%>        <div id="estadisticas" class="vista-activa d-none">

            <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">

                <div>

                    <h3 class="m-0 fw-bold"><i class="bi bi-graph-up-arrow me-2" style="color: #c084fc;"></i>Analítica en Tiempo Real y Estadísticas Clínicas</h3>

                    <p class="text-secondary m-0 small">Monitoreo dinámico de ocupación, inventarios y especialidades del hospital</p>

                </div>

                <div class="d-flex gap-2">

                    <button class="btn btn-outline-primary btn-sm rounded-pill px-3" onclick="actualizarGraficos()"><i class="bi bi-arrow-clockwise me-1"></i>Actualizar Datos</button>

                </div>

            </div>



            <div class="row g-4 mb-4">

                <div class="col-md-4">

                    <div class="stat-card p-4 rounded-4 h-100" style="background: var(--bg-panel); border: var(--glass-border); backdrop-filter: blur(15px);">

                        <h5 class="fw-bold mb-3 text-info"><i class="bi bi-pie-chart-fill me-2"></i>Especialidades Demandadas</h5>

                        <div style="position: relative; height: 260px; width: 100%;">

                            <canvas id="chartEspecialidades"></canvas>

                        </div>

                    </div>

                </div>

                <div class="col-md-4">

                    <div class="stat-card p-4 rounded-4 h-100" style="background: var(--bg-panel); border: var(--glass-border); backdrop-filter: blur(15px);">

                        <h5 class="fw-bold mb-3 text-success"><i class="bi bi-bar-chart-fill me-2"></i>Estado de Citas Médicas</h5>

                        <div style="position: relative; height: 260px; width: 100%;">

                            <canvas id="chartCitasEstado"></canvas>

                        </div>

                    </div>

                </div>

                <div class="col-md-4">

                    <div class="stat-card p-4 rounded-4 h-100" style="background: var(--bg-panel); border: var(--glass-border); backdrop-filter: blur(15px);">

                        <h5 class="fw-bold mb-3 text-warning"><i class="bi bi-doughnut-chart me-2"></i>Disponibilidad de Bodega</h5>

                        <div style="position: relative; height: 260px; width: 100%;">

                            <canvas id="chartStockMeds"></canvas>

                        </div>

                    </div>

                </div>

            </div>

        </div>








