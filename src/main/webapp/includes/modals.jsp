<%@ page pageEncoding="UTF-8" %>
<%@ page import="java.util.List,java.util.Map" %>
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
%><%@ page import="java.util.List, java.util.Map, java.util.ArrayList, com.nurselogic.model.*" %>

        <!-- Modal Cambio de Rol -->
<div class="modal fade" id="modalRol" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-shield-lock me-2 text-primary"></i>Cambiar Rol de Usuario
                </h5>
                <button type="button" class="btn-close btn-close-white" onclick="cerrarModalRol()"></button>
            </div>
            <div class="modal-body">
                <p class="text-secondary small mb-3">Selecciona el nuevo nivel de acceso para <span id="rolUserEmail" class="fw-bold text-theme"></span></p>
                <select id="rolSelectModal" class="form-select form-select-lg mb-3" style="max-height: 200px; overflow-y: auto;" size="5">
                    <%
                        List<String> dynamicRoles = (List<String>) request.getAttribute("listaRoles");
                        if (dynamicRoles != null) {
                            for(String dr : dynamicRoles) {
                                out.print("<option value='" + dr + "'>" + dr + "</option>");
                            }
                        } else {
                            out.print("<option value='Admin'>Admin</option>");
                            out.print("<option value='M&eacute;dico'>M&eacute;dico</option>");
                            out.print("<option value='Paciente'>Paciente</option>");
                            out.print("<option value='Pendiente'>Pendiente</option>");
                        }
                    %>
                </select>
            </div>
            <div class="modal-footer border-0">
                <button class="btn btn-secondary px-4" onclick="cerrarModalRol()">Cancelar</button>
                <button type="button" class="btn btn-primary px-4 fw-bold" onclick="guardarCambioRol()">Guardar Cambios</button>
            </div>
        </div>
    </div>
</div>

<!-- Modal Nuevo Rol (Asistente con Plantillas) -->
<div class="modal fade" id="modalNuevoRol" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-magic me-2 text-warning"></i>Asistente de Creación
                </h5>
                <button type="button" class="btn-close btn-close-white" onclick="cerrarModalNuevoRol()"></button>
            </div>
            <form action="adminAction" method="POST" autocomplete="off">
                <div class="modal-body">
                    <input type="hidden" name="action" value="crearRol" autocomplete="off">

                    <p class="text-secondary small mb-2 fw-semibold">Paso 1: Elige un Molde / Plantilla base</p>
                    <div class="row g-2 mb-4">
                        <div class="col-md-3">
                            <div class="p-2 border rounded text-center plantilla-card" style="border-color: rgba(255,255,255,0.2) !important; cursor: pointer; background: rgba(255,255,255,0.05);" onclick="aplicarPlantillaRol('Moderador', this)">
                                <i class="bi bi-shield-check d-block fs-4 text-info mb-1"></i>
                                <span class="small fw-bold d-block">Moderador</span>
                                <span class="text-secondary" style="font-size: 0.7rem;">Gestión de personal</span>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-2 border rounded text-center plantilla-card" style="border-color: rgba(255,255,255,0.2) !important; cursor: pointer; background: rgba(255,255,255,0.05);" onclick="aplicarPlantillaRol('Bodeguero', this)">
                                <i class="bi bi-box-seam d-block fs-4 text-warning mb-1"></i>
                                <span class="small fw-bold d-block">Bodeguero</span>
                                <span class="text-secondary" style="font-size: 0.7rem;">Inventario y catálogos</span>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-2 border rounded text-center plantilla-card" style="border-color: rgba(255,255,255,0.2) !important; cursor: pointer; background: rgba(255,255,255,0.05);" onclick="aplicarPlantillaRol('Médico', this)">
                                <i class="bi bi-heart-pulse d-block fs-4 text-danger mb-1"></i>
                                <span class="small fw-bold d-block">Médico</span>
                                <span class="text-secondary" style="font-size: 0.7rem;">Pacientes y citas</span>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-2 border rounded text-center plantilla-card" style="border-color: rgba(255,255,255,0.2) !important; cursor: pointer; background: rgba(255,255,255,0.05);" onclick="aplicarPlantillaRol('Custom', this)">
                                <i class="bi bi-sliders d-block fs-4 text-secondary mb-1"></i>
                                <span class="small fw-bold d-block">A Medida</span>
                                <span class="text-secondary" style="font-size: 0.7rem;">Elige manual</span>
                            </div>
                        </div>
                    </div>

                    <p class="text-secondary small mb-2 fw-semibold">Paso 2: Define Detalles y Permisos</p>
                    <div class="row g-3">
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Nombre del Rol (Ej: Enfermera Jefe)</label>
                            <input type="text" name="nombreRol" class="form-control" style="background-color:rgba(0,0,0,0.2); color:#fff; border:1px solid rgba(255,255,255,0.1);" required autocomplete="off">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Descripción breve</label>
                            <input type="text" name="descRol" class="form-control" style="background-color:rgba(0,0,0,0.2); color:#fff; border:1px solid rgba(255,255,255,0.1);" required autocomplete="off">
                        </div>
                    </div>

                    <div class="mt-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.05);">
                        <label class="form-label small text-secondary fw-bold mb-3">
                            <i class="bi bi-toggles me-1"></i>Asignación de Permisos
                        </label>
                        <div class="row g-2">

                            <!-- COLUMNA IZQUIERDA — permisos CSV legacy -->
                            <div class="col-md-6">
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_inventario" name="permiso" value="Inventario" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_inventario">
                                        <i class="bi bi-capsule text-success me-1"></i>Inventario de Medicamentos
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_catalogos" name="permiso" value="Catálogos" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_catalogos">
                                        <i class="bi bi-folder2-open me-1" style="color:#60a5fa;"></i>Catálogos (Enfermedades/Alergias)
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_admision" name="permiso" value="Admision" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_admision">
                                        <i class="bi bi-person-plus text-info me-1"></i>Admisión y Triage de Pacientes
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_citas" name="permiso" value="Citas" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_citas">
                                        <i class="bi bi-calendar-check text-warning me-1"></i>Agendar y Control de Citas
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_reportes" name="permiso" value="Reportes" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_reportes">
                                        <i class="bi bi-graph-up-arrow me-1" style="color:#c084fc;"></i>Ver Reportes y Estadísticas
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_usuarios" name="permiso" value="Usuarios" autocomplete="off">
                                    <label class="form-check-label text-light small text-danger fw-bold" for="perm_usuarios">
                                        <i class="bi bi-shield-lock me-1"></i>Gestión de Usuarios (Admin)
                                    </label>
                                </div>
                            </div>

                            <!-- COLUMNA DERECHA — 5 permisos booleanos NUEVOS -->
                            <div class="col-md-6">
                                <p class="text-secondary small fw-semibold mb-2" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:4px;">
                                    Módulos del Sistema
                                </p>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_hosp" name="permBoolHosp" value="true" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_hosp">
                                        <i class="bi bi-hospital me-1" style="color:#22d3ee;"></i>Hospitalización y Camas
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_ventas" name="permBoolVentas" value="true" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_ventas">
                                        <i class="bi bi-receipt text-primary me-1"></i>Reporte de Ventas (Farmacia)
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_dirpac" name="permBoolDirPac" value="true" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_dirpac">
                                        <i class="bi bi-people text-info me-1"></i>Directorio de Pacientes
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_catclin" name="permBoolCatClin" value="true" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_catclin">
                                        <i class="bi bi-journal-medical me-1" style="color:#60a5fa;"></i>Catálogos Clínicos
                                    </label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox"
                                           id="perm_soporteti" name="permBoolSoporteTI" value="true" autocomplete="off">
                                    <label class="form-check-label text-light small" for="perm_soporteti">
                                        <i class="bi bi-headset me-1" style="color:#fbbf24;"></i>Soporte T.I.
                                    </label>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
                <div class="modal-footer border-0 pt-0 mt-3">
                    <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalNuevoRol()">Cancelar</button>
                    <button type="submit" class="btn btn-warning px-4 fw-bold text-dark"><i class="bi bi-check-circle me-1"></i>Crear Rol con Permisos</button>
                </div>
            </form>
        </div>
    </div>
</div>
<!-- END modalNuevoRol -->

<div class="modal fade" id="modalReceta" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(20px); border: var(--glass-border); box-shadow: 0 0 30px rgba(56, 189, 248, 0.2);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-prescription2 me-2"></i>Prescripci&oacute;n Electr&oacute;nica y Entrega de Farmacia
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <form action="adminAction" method="post" onsubmit="return validarFormularioReceta(event)" autocomplete="off">
                <input type="hidden" name="action" value="prescribirReceta" autocomplete="off">
                <input type="hidden" id="recetaEsNuevoPac" name="esNuevoPaciente" value="false" autocomplete="off">
                <input type="hidden" id="recetaPacienteIdHidden" name="pacienteId" value="" autocomplete="off">
                <div class="modal-body">
                    <div class="row g-3 mb-3">
                        <div class="col-md-12">
                            <label class="form-label small text-secondary fw-semibold">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
                            <input type="text" id="recetaCedula" name="cedula" class="form-control" style="border: var(--glass-border);" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteReceta(this.value);" required autocomplete="off">
                            <input type="hidden" id="recetaPacNombre" name="pacienteNombre" value="" autocomplete="off">
                            <div id="recetaPacNombreInfo" class="form-text text-info mt-1"></div>
                        </div>
                    </div>

                    <!-- QUICK REGISTER FALLBACK -->
                    <div id="recetaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
                        <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
                        <div class="row g-2">
                            <div class="col-md-6">
                                <input type="text" id="recetaNuevoNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <input type="text" id="recetaNuevoApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <input type="date" id="recetaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <select id="recetaNuevoSexo" name="nuevoSexo" class="form-select form-select-sm">
                                    <option value="">-- Sexo --</option>
                                    <option value="M">Masculino</option>
                                    <option value="F">Femenino</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label fw-semibold">Seleccionar Medicamento (Bodega)</label>
                        <div class="input-group">
                            <select id="selectMedicamentoAdd" class="form-select" style="border: var(--glass-border); background: #0f172a; color: white;">
                                <option value="">-- Seleccionar medicamento --</option>
                                <%
                                    List<Map<String, String>> medsReceta = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");
                                    if (medsReceta != null) {
                                        for (Map<String, String> mSel : medsReceta) {
                                            String safeNombre = mSel.get("nombre") != null ? mSel.get("nombre").replace("'", "").replace("\"", "") : "Medicamento";
                                            out.print("<option value='" + mSel.get("id") + "' data-nombre='" + safeNombre + "' data-stock='" + mSel.get("stock") + "'>" + safeNombre + " (Stock: " + mSel.get("stock") + ")</option>");
                                        }
                                    }
                                %>
                            </select>
                            <button type="button" class="btn btn-info px-3" onclick="agregarMedicamentoReceta()"><i class="bi bi-plus-lg me-1"></i> A&ntilde;adir</button>
                        </div>
                    </div>

                    <div class="p-3 mb-3 rounded" style="background: rgba(0,0,0,0.2); border: var(--glass-border); min-height: 80px;">
                        <small class="text-secondary fw-semibold d-block mb-2"><i class="bi bi-list-check me-1"></i> Medicamentos a Prescribir y Unidades por F&aacute;rmaco:</small>
                        <div id="msgRecetaVacia" class="text-secondary small text-center py-2">No hay medicamentos a&ntilde;adidos a&uacute;n.</div>
                        <div id="listaMedicamentosReceta"></div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">Indicaciones Dosis y Frecuencia</label>
                        <input type="text" name="indicaciones" class="form-control" placeholder="Ej: 1 tableta cada 8 horas por 5 d&iacute;as" required autocomplete="off">
                    </div>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-outline-info rounded-pill px-4 me-auto" onclick="imprimirRecetaPDF()"><i class="bi bi-printer-fill me-2"></i>Imprimir Receta PDF</button>
                    <button type="button" class="btn btn-secondary rounded-pill px-4" data-bs-dismiss="modal">Cancelar</button>
                    <button type="submit" id="btnPrescribirReceta" class="btn btn-success rounded-pill"><i class="bi bi-check-circle me-2"></i>Prescribir y Guardar</button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- AREA OCULTA DE IMPRESION PARA RECETA PDF (@media print) -->
<div id="areaImpresionReceta" class="d-none">
    <div style="text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px;">
        <h1 style="margin:0; font-size: 28px; color: #0b0f19;">CENTRO HOSPITALARIO NURSELOGIC</h1>
        <p style="margin:5px 0 0 0; font-size: 14px; color: #666;">Direcci&oacute;n M&eacute;dica Integral | Receta Oficial Electr&oacute;nica</p>
    </div>
    <div style="margin-bottom: 30px; line-height: 1.8; font-size: 16px;">
        <p><strong>Fecha de Prescripci&oacute;n:</strong> <span id="printFecha"></span></p>
        <p><strong>Paciente:</strong> <span id="printPac"></span></p>
        <p><strong>M&eacute;dico Tratante:</strong> <span id="printMed"><%= session.getAttribute("nombres") != null ? session.getAttribute("nombres") : "Usuario del Sistema" %> (<%= session.getAttribute("rol") %>)</span></p>
    </div>
    <div style="border: 1px solid #ccc; padding: 25px; border-radius: 8px; margin-bottom: 40px; background: #f9f9f9;">
        <h3 style="margin-top:0; border-bottom: 1px solid #ddd; padding-bottom: 10px; color: #0ea5e9;">Prescripci&oacute;n Farmacol&oacute;gica</h3>
        <p style="font-size: 18px; margin: 15px 0;"><strong>F&aacute;rmaco:</strong> <span id="printFarmaco"></span></p>
        <p style="font-size: 18px; margin: 15px 0;"><strong>Cantidad Prescrita:</strong> <span id="printCant"></span> unidades</p>
        <p style="font-size: 18px; margin: 15px 0;"><strong>Indicaciones / Dosis:</strong> <span id="printInd"></span></p>
    </div>
    <div style="margin-top: 80px; text-align: center;">
        <div style="display:inline-block; border-top: 1px solid #000; width: 300px; padding-top: 10px;">
            <strong>Firma del M&eacute;dico / Sello Cl&iacute;nico</strong><br>
            <small>Nurselogic Sistema de Gesti&oacute;n Hospitalaria</small>
        </div>
    </div>
</div>

<!-- Modal Añadir Cama -->
<div class="modal fade" id="modalAnadirCama" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(20px); border: var(--glass-border); box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-hospital-fill me-2"></i>A&ntilde;adir Nueva Cama
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <form action="camasAction" method="post" autocomplete="off">
                <input type="hidden" name="action" value="crear" autocomplete="off">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">N&uacute;mero de Cama</label>
                        <input type="text" name="numero" class="form-control" style="border: var(--glass-border);" placeholder="N&uacute;mero" required autocomplete="off">
                    </div>
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">Sala / &Aacute;rea Hospitalaria</label>
                        <select name="sala" class="form-select" style="border: var(--glass-border);" required>
                            <option value="Hospitalizaci&oacute;n General">Hospitalizaci&oacute;n General</option>
                            <option value="Urgencias">Urgencias</option>
                            <option value="UCI">UCI</option>
                            <option value="Pediatr&iacute;a">Pediatr&iacute;a</option>
                        </select>
                    </div>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary rounded-pill px-4" data-bs-dismiss="modal">Cancelar</button>
                    <button type="submit" class="btn btn-success rounded-pill"><i class="bi bi-plus-circle me-2"></i>A&ntilde;adir Cama</button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- Modal Internar Cama -->
<div class="modal fade" id="modalInternarCama" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(20px); border: var(--glass-border); box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-hospital-fill me-2"></i>Internar Paciente en Cama <span id="internarCamaNumLabel"></span>
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <form action="camasAction" method="post" autocomplete="off">
                <input type="hidden" name="action" value="asignar" autocomplete="off">
                <input type="hidden" id="internarIdCama" name="camaId" value="" autocomplete="off">
                <input type="hidden" id="camaEsNuevoPac" name="esNuevoPaciente" value="false" autocomplete="off">
                <input type="hidden" id="camaPacienteIdHidden" name="pacienteId" value="" autocomplete="off">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
                        <input type="text" id="camaCedula" name="cedula" class="form-control" style="border: var(--glass-border);" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteCama(this.value);" required autocomplete="off">
                        <div id="camaPacNombreInfo" class="form-text text-info mt-1"></div>
                    </div>

                    <!-- QUICK REGISTER FALLBACK -->
                    <div id="camaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
                        <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
                        <div class="row g-2">
                            <div class="col-md-6">
                                <input type="text" id="camaNuevoNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <input type="text" id="camaNuevoApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <input type="date" id="camaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>" autocomplete="off">
                            </div>
                            <div class="col-md-6">
                                <select id="camaNuevoSexo" name="nuevoSexo" class="form-select form-select-sm">
                                    <option value="">-- Sexo --</option>
                                    <option value="M">Masculino</option>
                                    <option value="F">Femenino</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">Médico de Turno / Asignado</label>
                        <input type="text" id="camaMedico" name="medicoNombre" class="form-control" style="border: var(--glass-border);" placeholder="Ej: Dr. Juan Pérez" required autocomplete="off">
                    </div>
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">Motivo de Internación (Corto)</label>
                        <input type="text" id="camaMotivo" name="motivo" class="form-control" style="border: var(--glass-border);" placeholder="Ej: Observación Post-Quirúrgica" required autocomplete="off">
                    </div>
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">Diagnóstico de Ingreso Detallado</label>
                        <textarea id="camaDiagnostico" name="diagnostico" class="form-control" rows="3" style="border: var(--glass-border);" placeholder="Detalles de la internación, síntomas y estado general..." required></textarea>
                    </div>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary rounded-pill px-4" data-bs-dismiss="modal">Cancelar</button>
                    <button type="submit" id="btnInternarCama" class="btn btn-success rounded-pill"><i class="bi bi-check2-square me-2"></i>Asignar y Ocupar Cama</button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- Modal Ver Diagnóstico -->
<div class="modal fade" id="modalVerDiagnostico" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-file-medical-fill me-2 text-info"></i>Historial Clínico - <span id="verDiagPaciente" class="text-info"></span></h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
          <div class="mb-4">
              <h6 class="fw-bold text-secondary"><i class="bi bi-journal-medical me-2"></i>Diagnóstico</h6>
              <div class="p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); white-space: pre-wrap;" id="verDiagTexto"></div>
          </div>
          <div>
              <h6 class="fw-bold text-secondary"><i class="bi bi-capsule me-2"></i>Receta Médica</h6>
              <div class="p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); white-space: pre-wrap;" id="verDiagReceta"></div>
          </div>
      </div>
      <div class="modal-footer border-0">
        <button type="button" class="btn btn-outline-info px-4 me-auto" onclick="imprimirFactura()"><i class="bi bi-printer"></i> Imprimir</button>
          <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal Atender Cita (Smart UI) -->
<div class="modal fade" id="modalAtenderCita" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-heart-pulse-fill me-2 text-danger"></i>Consulta M&eacute;dica Avanzada - <span id="atenderCitaPaciente" class="text-info"></span></h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>

      <form action="adminAction" method="post" id="formAtenderCita" autocomplete="off">
        <input type="hidden" name="action" value="atenderCita" autocomplete="off">
        <input type="hidden" name="idCita" id="atenderIdCita" autocomplete="off">
        <input type="hidden" name="pacienteNombre" id="atenderPacNombre" autocomplete="off">

        <div class="modal-body p-0">
            <!-- Pestañas (Tabs) -->
            <ul class="nav nav-pills nav-justified p-3" id="consultaTabs" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="vitales-tab" data-bs-toggle="pill" data-bs-target="#vitales" type="button" role="tab" style="border-radius: 8px;"><i class="bi bi-activity me-1"></i> Signos Vitales</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link mx-2" id="glasgow-tab" data-bs-toggle="pill" data-bs-target="#glasgow" type="button" role="tab" style="border-radius: 8px;"><i class="bi bi-eye-fill me-1"></i> Glasgow</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="diag-tab" data-bs-toggle="pill" data-bs-target="#diag" type="button" role="tab" style="border-radius: 8px;"><i class="bi bi-journal-medical me-1"></i> Diagn&oacute;stico & Receta</button>
              </li>
            </ul>

            <!-- Contenido de Pestañas -->
            <div class="tab-content px-4 pb-4" id="consultaTabsContent" style="min-height: 250px;">

                <!-- Tab Signos Vitales -->
                <div class="tab-pane fade show active" id="vitales" role="tabpanel">
                    <div class="row g-3">
                        <div class="col-md-4">
                            <label class="form-label small text-secondary">Frecuencia Card&iacute;aca (lpm)</label>
                            <input type="number" id="atender_fc_input" class="form-control" placeholder="Ej: 80" min="0" oninput="if(typeof formatearFC === 'function') formatearFC(this); if(typeof evaluarVitales === 'function') evaluarVitales();" autocomplete="off">
                            <div id="atender_fc_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary">Presi&oacute;n Arterial (Sist/Diast)</label>
                            <input type="text" id="atender_pa_input" class="form-control" placeholder="Ej: 120/80" onkeyup="if(typeof formatearPresion === 'function') formatearPresion(this);" oninput="if(typeof evaluarVitales === 'function') evaluarVitales();" autocomplete="off">
                            <div id="atender_pa_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary">Frecuencia Respiratoria</label>
                            <input type="number" id="atender_fr_input" class="form-control" placeholder="Ej: 16" min="0" oninput="if(typeof formatearFR === 'function') formatearFR(this); if(typeof evaluarVitales === 'function') evaluarVitales();" autocomplete="off">
                            <div id="atender_fr_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Saturaci&oacute;n O2 (%)</label>
                            <input type="number" id="atender_sat_input" class="form-control" placeholder="Ej: 98" min="0" oninput="if(typeof formatearSat === 'function') formatearSat(this); if(typeof evaluarVitales === 'function') evaluarVitales();" autocomplete="off">
                            <div id="atender_sat_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Temperatura (&deg;C)</label>
                            <input type="number" step="0.1" id="atender_temp_input" class="form-control" placeholder="Ej: 37.0" min="0" oninput="if(typeof formatearTemperatura === 'function') formatearTemperatura(this); if(typeof evaluarVitales === 'function') evaluarVitales();" autocomplete="off">
                            <div id="atender_temp_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                    </div>
                </div>

                <!-- Tab Glasgow -->
                <div class="tab-pane fade" id="glasgow" role="tabpanel">
                    <div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-color);">
                        <h6 class="m-0 text-info fw-bold">Puntaje Total Glasgow:</h6>
                        <span id="glasgowTotal" class="badge bg-primary fs-5 px-3">15 / 15</span>
                        <span id="glasgowDesc" class="fw-bold text-success">Normal</span>
                    </div>
                    <div class="row g-3">
                        <div class="col-12">
                            <label class="form-label small text-secondary">Apertura Ocular (1-4)</label>
                            <select id="g_ocular" class="form-select" onchange="calcularGlasgow()">
                                <option value="4">4 - Espont&aacute;nea</option>
                                <option value="3">3 - A la orden verbal</option>
                                <option value="2">2 - Al dolor</option>
                                <option value="1">1 - Sin respuesta</option>
                            </select>
                        </div>
                        <div class="col-12">
                            <label class="form-label small text-secondary">Respuesta Verbal (1-5)</label>
                            <select id="g_verbal" class="form-select" onchange="calcularGlasgow()">
                                <option value="5">5 - Orientado y conversando</option>
                                <option value="4">4 - Desorientado / Confuso</option>
                                <option value="3">3 - Palabras inapropiadas</option>
                                <option value="2">2 - Sonidos incomprensibles</option>
                                <option value="1">1 - Sin respuesta</option>
                            </select>
                        </div>
                        <div class="col-12">
                            <label class="form-label small text-secondary">Respuesta Motora (1-6)</label>
                            <select id="g_motora" class="form-select" onchange="calcularGlasgow()">
                                <option value="6">6 - Obedece &oacute;rdenes</option>
                                <option value="5">5 - Localiza el dolor</option>
                                <option value="4">4 - Retirada y flexi&oacute;n normal</option>
                                <option value="3">3 - Flexi&oacute;n anormal (Decorticaci&oacute;n)</option>
                                <option value="2">2 - Extensi&oacute;n (Descerebraci&oacute;n)</option>
                                <option value="1">1 - Sin respuesta</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Tab Diagnostico y Receta -->
                <div class="tab-pane fade" id="diag" role="tabpanel">
                    <label class="form-label small text-secondary">Diagn&oacute;stico Cl&iacute;nico</label>
                    <textarea name="diagnostico" id="diagnosticoFinal" class="form-control mb-3" rows="4" placeholder="Describa el diagn&oacute;stico, s&iacute;ntomas y observaciones..." required></textarea>

                    <label class="form-label small text-secondary">Receta M&eacute;dica / Prescripci&oacute;n (Opcional)</label>
                    <textarea name="receta" id="recetaFinal" class="form-control" rows="3" placeholder="Medicamentos, dosis y recomendaciones..."></textarea>
                </div>

            </div>
        </div>

        <div class="modal-footer border-0 p-3" style="background: rgba(0,0,0,0.1);">
            <button type="button" class="btn btn-secondary px-4 rounded-pill" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-danger px-4 rounded-pill fw-bold" onclick="prepararYEnviarConsulta()"><i class="bi bi-check-circle me-2"></i>Finalizar Consulta</button>
        </div>
      </form>
    </div>
  </div>
</div>


<!-- Burbuja Flotante Carrito -->
<div id="cartBubbleContainer" class="position-fixed bottom-0 end-0 p-4 d-none" style="z-index: 1050;">
    <button type="button" class="btn btn-info rounded-circle shadow-lg p-3 position-relative" style="width: 60px; height: 60px;" onclick="abrirModalCarrito()">
        <i class="bi bi-cart3 fs-4 text-dark"></i>
        <span id="cartBubbleBadge" class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger shadow-sm" style="font-size: 0.85rem;">
            0
        </span>
    </button>
</div>

<!-- Modal Carrito de Ventas -->
<div class="modal fade" id="modalCarrito" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-cart-check me-2 text-info"></i>Carrito de Facturación</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body pb-0">
          <div class="row mb-3 px-2">
              <div class="col-md-5">
                  <label class="form-label text-secondary small mb-1">Cédula del Cliente</label>
                  <div class="input-group input-group-sm">
                      <span class="input-group-text bg-transparent text-secondary border-secondary"><i class="bi bi-person-badge"></i></span>
                      <input type="text" id="ventaCedulaCarrito" class="form-control bg-transparent text-white border-secondary" placeholder="10 dígitos..." maxlength="10" oninput="buscarClienteCarrito(this.value)">
                  </div>
              </div>
              <div class="col-md-7">
                  <label class="form-label text-secondary small mb-1">Nombre del Cliente</label>
                  <input type="text" id="ventaClienteCarrito" class="form-control form-control-sm bg-transparent text-white border-secondary" placeholder="Consumidor Final" oninput="if(this.value.trim() !== '') { this.classList.add('fw-bold', 'text-info'); } else { this.classList.remove('fw-bold', 'text-info'); }">
              </div>
          </div>
          <div class="table-responsive">
            <table class="table table-dark-custom table-sm">
                <thead>
                    <tr>
                        <th>Fármaco</th>
                        <th>Precio U.</th>
                        <th style="width: 120px;">Cantidad</th>
                        <th>Subtotal</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="tablaCarritoCuerpo">
                    <!-- Dinamico -->
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3" class="text-end fw-bold">TOTAL:</td>
                        <td colspan="2" class="text-success fw-bold fs-5" id="carritoTotalLabel">.00</td>
                    </tr>
                </tfoot>
            </table>
        </div>
      </div>
      <div class="modal-footer border-0 pt-0 mt-2 d-flex justify-content-between w-100">
        <button type="button" class="btn btn-outline-danger px-3" onclick="vaciarCarrito()"><i class="bi bi-trash"></i> Cancelar</button>
        <div>
            <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Seguir</button>
            <button type="button" class="btn btn-success px-4 fw-bold shadow-sm text-dark" onclick="procesarCheckout()"><i class="bi bi-receipt me-1"></i>Facturar</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Modal Añadir Stock Múltiple -->
<div class="modal fade" id="modalAnadirStockMultiple" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-box-seam me-2" style="color:#a3e635;"></i>Abastecimiento de Bodega</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body pb-0">
        <div class="alert alert-info py-2 small bg-opacity-10 border-0"><i class="bi bi-info-circle me-1"></i> Selecciona uno o varios fármacos y asigna cuántas unidades nuevas ingresan a bodega.</div>
        <div class="mb-3">
            <label class="form-label small text-secondary">Fármacos a abastecer</label>
            <select id="selectStockMultiple" class="form-select" multiple size="6" onchange="renderizarCamposStock()">
                <!-- Opciones se llenan por JS -->
            </select>
            <div class="form-text text-secondary">Mantén presionado Ctrl (o Cmd) para seleccionar múltiples.</div>
        </div>
        <div id="camposStockDinamicos" class="row g-2 mb-3">
            <!-- Campos dinámicos -->
        </div>
      </div>
      <div class="modal-footer border-0 pt-0 mt-3">
        <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cancelar</button>
        <button type="button" class="btn px-4 fw-bold shadow-sm text-dark" style="background: linear-gradient(135deg, #a3e635, #84cc16);" onclick="procesarAbastecimiento()"><i class="bi bi-check-lg me-1"></i>Registrar Ingreso</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal Facturar Venta -->
<div class="modal fade" id="modalFacturarVenta" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content text-theme" style="background-color: #1a2235; border: 1px solid #2d3748; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-receipt me-2"></i>Facturaci&oacute;n de Venta de Farmacia
                </h5>
                <button type="button" class="btn-close btn-close-white" aria-label="Close" onclick="cerrarModalVenta()"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label class="form-label fw-semibold">Nombre del Cliente / Paciente</label>
                    <input type="text" id="ventaCliente" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" placeholder="Consumidor Final" required autocomplete="off">
                </div>
                <div class="mb-3">
                    <label class="form-label fw-semibold">Medicamento a Vender</label>
                    <input type="text" id="ventaNombreMed" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" disabled autocomplete="off">
                </div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label fw-semibold">Cantidad (Max: <span id="ventaMaxStock"></span>)</label>
                        <input type="number" id="ventaCantidad" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" min="1" value="1" oninput="calcTotalVenta()" autocomplete="off">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label fw-semibold">Total a Pagar</label>
                        <input type="text" id="ventaTotal" class="form-control text-success fw-bold" style="background-color:#0b0f19; border:1px solid #374151;" disabled autocomplete="off">
                    </div>
                </div>
            </div>
            <div class="modal-footer border-0">
                <button class="btn btn-secondary" style="background-color:#4b5563; border:none; border-radius:8px;" onclick="cerrarModalVenta()">Cancelar</button>
                <button type="button" class="btn btn-primary" style="background-color:#10b981; border:none; border-radius:8px;" onclick="confirmarVenta()">Confirmar y Generar PDF</button>
            </div>
        </div>
    </div>
</div>

<div id="areaImpresionFactura" style="display:none; font-family: monospace; color:#000; background:#fff; padding:20px; width:400px;">
    <h2 style="text-align:center; font-family:sans-serif; margin-bottom:5px;">NURSELOGIC FARMACIA</h2>
    <p style="text-align:center; font-size:12px; margin-top:0;">FACTURA DE VENTA ELECTRÓNICA</p>
    <hr style="border: 1px dashed #000;">
    <p><strong>Fecha: </strong> <span id="facFecha"></span></p>
    <p><strong>Cliente: </strong> <span id="facCliente"></span></p>
    <hr style="border: 1px dashed #000;">
    <table style="width:100%; text-align:left;">
        <thead>
            <tr>
                <th>CANT</th>
                <th>DESCRIPCIÓN</th>
                <th style="text-align:right;">SUBT</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td id="facCant"></td>
                <td id="facDesc"></td>
                <td id="facSubt" style="text-align:right;"></td>
            </tr>
        </tbody>
    </table>
    <hr style="border: 1px dashed #000;">
    <h3 style="text-align:right;">TOTAL: $<span id="facTotal"></span></h3>
    <p style="text-align:center; font-size:10px; margin-top:30px;">Gracias por su compra. Conserve esta factura.</p>
</div>

<!-- Modal Especialidad -->
<div class="modal fade" id="modalEspecialidad" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-award me-2 text-warning"></i>Asignar Especialidad Clínica</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalEspecialidad()"></button>
      </div>
      <form action="adminAction" method="POST" autocomplete="off">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="editarEspecialidad" autocomplete="off">
          <input type="hidden" name="target" value="usuario" autocomplete="off">
          <input type="hidden" name="id" id="espUserEmail" autocomplete="off">
          <p class="text-secondary small mb-3">Selecciona la especialidad médica para <span id="espUserDisplay" class="fw-bold text-theme"></span></p>
          <select name="nuevaEspecialidad" id="selectEspecialidadModal" class="form-select form-select-lg mb-3" style="max-height: 200px; overflow-y: auto;" size="5">
              <%
                  List<String> dynamicEsps = (List<String>) request.getAttribute("listaEspecialidades");
                  if (dynamicEsps != null && !dynamicEsps.isEmpty()) {
                      for(String de : dynamicEsps) {
                          out.print("<option value='" + de + "'>" + de + "</option>");
                      }
                  } else {
                      out.print("<option value='Medicina General'>Medicina General</option>");
                      out.print("<option value='Pediatría'>Pediatría</option>");
                      out.print("<option value='Cardiología'>Cardiología</option>");
                  }
              %>
          </select>
        </div>
        <div class="modal-footer border-0 pt-0">
          <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalEspecialidad()">Cancelar</button>
          <button type="submit" class="btn btn-warning px-4 text-dark fw-bold">Guardar Cambios</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Modal Nueva Especialidad -->
<div class="modal fade" id="modalNuevaEspecialidad" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-award-fill me-2 text-info"></i>Crear Nueva Especialidad</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalNuevaEspecialidad()"></button>
      </div>
      <form action="adminAction" method="POST" autocomplete="off">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="crearEspecialidad" autocomplete="off">
          <div class="mb-3">
             <label class="form-label small text-secondary">Nombre de la Especialidad</label>
             <input type="text" name="nombreEspecialidad" class="form-control" placeholder="Ej: Pediatría, Cardiología" required autocomplete="off">
          </div>
        </div>
        <div class="modal-footer border-0 pt-0">
          <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalNuevaEspecialidad()">Cancelar</button>
          <button type="submit" class="btn btn-info px-4 text-white fw-bold">Crear Especialidad</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Modal Medicamento -->
<div class="modal fade" id="modalMedicamento" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-capsule me-2 text-success"></i>Registrar Nuevo Medicamento</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalMedicamento()"></button>
      </div>
      <form action="adminAction" method="POST" autocomplete="off">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="crearMedicamento" autocomplete="off">
          <div class="mb-3">
             <label class="form-label small text-secondary">Nombre Farmacológico</label>
             <input type="text" name="nombreMed" class="form-control" required autocomplete="off">
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Presentación</label>
             <input type="text" name="presentacion" class="form-control" placeholder="Ej: Tabletas 500mg" required autocomplete="off">
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Stock Inicial</label>
             <input type="number" name="stockMed" class="form-control" min="0" value="0" required autocomplete="off">
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Precio Unitario ($)</label>
             <input type="number" name="precioMed" step="0.01" class="form-control" min="0" value="0.00" required autocomplete="off">
          </div>
        </div>
        <div class="modal-footer border-0 pt-0 mt-3">
          <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalMedicamento()">Cancelar</button>
          <button type="submit" class="btn btn-success px-4">Guardar</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Modal Catálogos -->
<div class="modal fade" id="modalCatalogos" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold" id="catModalTitulo"><i class="bi bi-folder-plus me-2 text-info"></i>Nuevo Elemento de Catálogo</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalCatalogos()"></button>
      </div>
      <form action="adminAction" method="POST" autocomplete="off">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" id="catActionInput" value="crearEnfermedad" autocomplete="off">
          <input type="hidden" name="idEnf" id="catIdEnf" autocomplete="off">
          <input type="hidden" name="idAle" id="catIdAle" autocomplete="off">

          <div id="catEnfermedadCampos" class="mb-3">
             <label class="form-label small text-secondary">Nombre de la Patología</label>
             <input type="text" name="nombreEnf" id="catNombreEnf" class="form-control" autocomplete="off">
             <label class="form-label small text-secondary mt-2">Descripción</label>
             <textarea name="descEnf" id="catDescEnf" class="form-control" rows="2"></textarea>
          </div>

          <div id="catAlergiaCampos" class="mb-3 d-none">
             <label class="form-label small text-secondary">Nombre del Alérgeno</label>
             <input type="text" name="nombreAle" id="catNombreAle" class="form-control" autocomplete="off">
             <label class="form-label small text-secondary mt-2">Gravedad</label>
             <select name="gravedadAle" id="catGravAle" class="form-select">
                <option value="Leve">Leve</option>
                <option value="Medio">Medio</option>
                <option value="Alto">Alto</option>
             </select>
          </div>
        </div>
        <div class="modal-footer border-0 pt-0 mt-3">
          
          <button type="submit" class="btn btn-primary px-4">Guardar</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Modal Nueva Cita Admin -->
<div class="modal fade" id="modalNuevaCitaAdmin" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-calendar-plus me-2 text-info"></i>Agendar Cita (Admin)</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalCitaAdmin()"></button>
      </div>
      <form action="agendarCita" method="POST" onsubmit="return validarCitaAdmin(event)" autocomplete="off">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="crearCitaAdmin" autocomplete="off">
          <input type="hidden" id="citaEsNuevoPac" name="esNuevoPaciente" value="false" autocomplete="off">

          <div class="mb-3">
             <label class="form-label small text-secondary">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
             <input type="hidden" id="citaPacienteIdHidden" name="pacienteId" autocomplete="off">
             <input type="text" id="citaCedula" name="cedula" class="form-control" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteCita(this.value);" required autocomplete="off">
             <div id="citaPacNombre" class="form-text text-info mt-1"></div>
          </div>
          
          <!-- QUICK REGISTER FALLBACK -->
          <div id="citaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
              <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
              <div class="row g-2">
                  <div class="col-md-6">
                      <input type="text" id="citaNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos" autocomplete="off">
                  </div>
                  <div class="col-md-6">
                      <input type="text" id="citaApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos" autocomplete="off">
                  </div>
                  <div class="col-md-6">
                      <input type="date" id="citaFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento" max="<%= java.time.LocalDate.now().toString() %>" autocomplete="off">
                  </div>
                  <div class="col-md-6">
                      <select id="citaSexo" name="nuevoSexo" class="form-select form-select-sm">
                          <option value="">-- Sexo --</option>
                          <option value="M">Masculino</option>
                          <option value="F">Femenino</option>
                      </select>
                  </div>
              </div>
          </div>

          <div class="mb-3">
             <label class="form-label small text-secondary">Especialidad</label>
             <select name="especialidad" class="form-select" required>
                <option value="1">Medicina General</option>
                <option value="2">Cardiolog&iacute;a</option>
                <option value="3">Pediatr&iacute;a</option>
                <option value="4">Neurolog&iacute;a</option>
                <option value="5">Ginecolog&iacute;a</option>
             </select>
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Fecha y Hora</label>
             <input type="datetime-local" id="citaFechaHora" name="fechaHora" class="form-control" required autocomplete="off">
          </div>
        </div>
        <div class="modal-footer border-0 pt-0 mt-3">
          <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalCitaAdmin()">Cancelar</button>
          <button type="submit" id="btnAgendarCita" class="btn btn-info px-4 text-dark fw-bold">Agendar</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Modal Ficha Clinica y Diagnostico Inteligente -->
<div class="modal fade" id="modalFichaClinica" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0 pb-0">
        <div>
          <h4 class="modal-title fw-bold text-info"><i class="bi bi-file-earmark-medical me-2"></i>Ficha Mdica Integral</h4>
          <h5 class="fw-bold m-0 mt-1 text-light" id="fichaNombre">---</h5>
          <small class="text-secondary" id="fichaInfo">Cédula: -- | Nacimiento: -- | Sexo: --</small>
        </div>
        <button type="button" class="btn-close btn-close-white align-self-start" onclick="cerrarModalFicha()"></button>
      </div>
      <div class="modal-body p-4">
        
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h6 class="fw-bold text-primary m-0"><i class="bi bi-heart-pulse-fill text-danger me-2"></i>Evaluación Clínica (Última)</h6>
            <span class="badge bg-secondary py-2 px-3" id="fichaFechaActualizacion"><i class="bi bi-calendar3 me-1"></i> Fecha: --</span>
        </div>
        
        <div class="table-responsive">
            <table class="table table-bordered table-dark-custom mb-4" style="background: rgba(255,255,255,0.02); border-color: rgba(255,255,255,0.1);">
                <tbody>
                    <tr>
                        <td class="fw-bold text-secondary" style="width: 25%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometría</td>
                        <td id="fichaEstPeso" class="fw-semibold text-light">-- / --</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-thermometer-half me-2 text-warning"></i>Temperatura</td>
                        <td id="fichaTemp" class="fw-bold text-warning">-- C</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-heart-pulse-fill me-2 text-danger"></i>Presión Arterial</td>
                        <td id="fichaPresion" class="fw-bold text-info">--</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-activity me-2 text-success"></i>Pulso / Sat. O2</td>
                        <td id="fichaFcSat" class="fw-bold text-success">-- / --</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-virus me-2" style="color: #c084fc;"></i>Enfermedades</td>
                        <td id="fichaEnfermedades" class="text-light">Ninguna</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-exclamation-triangle-fill me-2 text-danger"></i>Alergias</td>
                        <td id="fichaAlergias" class="fw-bold text-danger">Ninguna</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <h6 class="fw-bold text-info mb-3"><i class="bi bi-cpu me-1"></i>Inteligencia Clínica</h6>
        <div id="fichaAlertasContenedor">
          <!-- Contenido generado dinmicamente -->
        </div>
      </div>

      <div class="modal-footer border-0 pt-0">
        <button type="button" class="btn btn-outline-warning rounded-pill px-4" onclick="editarPacienteDesdeFicha()"><i class="bi bi-pencil-square me-1"></i>Editar Paciente</button>
        <button type="button" class="btn btn-secondary rounded-pill px-4" onclick="cerrarModalFicha()">Cerrar</button>
      </div>
    </div>
  </div>
</div>
<!-- Modal Ver Factura -->
<div class="modal fade" id="modalVerFactura" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-receipt me-2 text-info"></i>Detalle de Venta <span id="verFacId" class="text-info"></span></h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
          <div class="mb-3 d-flex justify-content-between">
              <div><small class="text-secondary">Cliente:</small><br><span class="fw-bold" id="verFacCliente"></span></div>
              <div class="text-end"><small class="text-secondary">Fecha:</small><br><span id="verFacFecha"></span></div>
          </div>
          <hr style="border-color: rgba(255,255,255,0.1);">
          <h6 class="fw-bold text-secondary mb-3">Artículos</h6>
          <div class="p-3 rounded mb-3" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1);" id="verFacDetalles"></div>
          <div class="text-end fs-5">
              <span class="text-secondary">Total Pagado:</span> <strong class="text-success">$<span id="verFacTotal"></span></strong>
          </div>
      </div>
      <div class="modal-footer border-0">
        <button type="button" class="btn btn-outline-info px-4 me-auto" onclick="imprimirFactura()"><i class="bi bi-printer"></i> Imprimir</button>
          <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>


