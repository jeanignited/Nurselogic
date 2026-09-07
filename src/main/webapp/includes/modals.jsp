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

<i class="bi bi-shield-lock me-2 text-primary"></i>Cambiar Rol de Usuario</h5>



                        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalRol()"></button>



                    

</div>

<div class="modal-body">

<p class="text-secondary small mb-3">Selecciona el nuevo nivel de acceso para <span id="rolUserEmail" class="fw-bold text-theme"></span></p>



                        <select id="rolSelectModal" class="formÃ¡select formÃ¡select-lg mb-3">



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
            <form action="adminAction" method="POST">
                <div class="modal-body">
                    <input type="hidden" name="action" value="crearRol">
                    
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
                            <input type="text" name="nombreRol" class="form-control" style="background-color:rgba(0,0,0,0.2); color:#fff; border:1px solid rgba(255,255,255,0.1);" required>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Descripción breve</label>
                            <input type="text" name="descRol" class="form-control" style="background-color:rgba(0,0,0,0.2); color:#fff; border:1px solid rgba(255,255,255,0.1);" required>
                        </div>
                    </div>
                    
                    <div class="mt-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.05);">
                        <label class="form-label small text-secondary fw-bold mb-3">Asignación de Permisos (Checkboxes)</label>
                        <div class="row g-2">
                            <div class="col-md-6">
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Inventario">
                                    <label class="form-check-label text-light small">Inventario de Medicamentos</label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Catálogos">
                                    <label class="form-check-label text-light small">Catálogos (Enfermedades)</label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Admision">
                                    <label class="form-check-label text-light small">Admisión y Triage de Pacientes</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Citas">
                                    <label class="form-check-label text-light small">Agendar y Control de Citas</label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Reportes">
                                    <label class="form-check-label text-light small">Ver Reportes y Estadísticas</label>
                                </div>
                                <div class="form-check form-switch mb-2">
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Usuarios">
                                    <label class="form-check-label text-light small text-danger fw-bold">Gestión de Usuarios (Admin)</label>
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
            <form action="adminAction" method="post" onsubmit="return validarFormularioReceta(event)">
                <input type="hidden" name="action" value="prescribirReceta">
                <input type="hidden" id="recetaEsNuevoPac" name="esNuevoPaciente" value="false">
                <input type="hidden" id="recetaPacienteIdHidden" name="pacienteId" value="">
                <div class="modal-body">
                    <div class="row g-3 mb-3">
                        <div class="col-md-12">
                            <label class="form-label small text-secondary fw-semibold">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
                            <input type="text" id="recetaCedula" name="cedula" class="form-control" style="border: var(--glass-border);" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteReceta(this.value);" required>
                            <input type="hidden" id="recetaPacNombre" name="pacienteNombre" value="">
                            <div id="recetaPacNombreInfo" class="form-text text-info mt-1"></div>
                        </div>
                    </div>

                    <!-- QUICK REGISTER FALLBACK -->
                    <div id="recetaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
                        <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
                        <div class="row g-2">
                            <div class="col-md-6">
                                <input type="text" id="recetaNuevoNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos">
                            </div>
                            <div class="col-md-6">
                                <input type="text" id="recetaNuevoApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos">
                            </div>
                            <div class="col-md-6">
                                <input type="date" id="recetaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento">
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
                        <input type="text" name="indicaciones" class="form-control" placeholder="Ej: 1 tableta cada 8 horas por 5 d&iacute;as" required>
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
</div><!-- Modal Añadir Cama -->
<div class="modal fade" id="modalAñadirCama" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(20px); border: var(--glass-border); box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);">
            <div class="modal-header border-0">
                <h5 class="modal-title fw-bold">
                    <i class="bi bi-hospital-fill me-2"></i>A&ntilde;adir Nueva Cama
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <form action="camasAction" method="post">
                <input type="hidden" name="action" value="crear">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">N&uacute;mero de Cama</label>
                        <input type="text" name="numero" class="form-control" style="border: var(--glass-border);" placeholder="N&uacute;mero" required>
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
            <form action="camasAction" method="post">
                <input type="hidden" name="action" value="asignar">
                <input type="hidden" id="internarIdCama" name="camaId" value="">
                <input type="hidden" id="camaEsNuevoPac" name="esNuevoPaciente" value="false">
                <input type="hidden" id="camaPacienteIdHidden" name="pacienteId" value="">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label small text-secondary fw-semibold">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
                        <input type="text" id="camaCedula" name="cedula" class="form-control" style="border: var(--glass-border);" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteCama(this.value);" required>
                        <div id="camaPacNombreInfo" class="form-text text-info mt-1"></div>
                    </div>

                    <!-- QUICK REGISTER FALLBACK -->
                    <div id="camaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
                        <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
                        <div class="row g-2">
                            <div class="col-md-6">
                                <input type="text" id="camaNuevoNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos">
                            </div>
                            <div class="col-md-6">
                                <input type="text" id="camaNuevoApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos">
                            </div>
                            <div class="col-md-6">
                                <input type="date" id="camaNuevoFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento">
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
                        <label class="form-label small text-secondary fw-semibold">Motivo de Internaci&oacute;n</label>
                        <input type="text" id="camaMotivo" name="motivo" class="form-control" style="border: var(--glass-border);" placeholder="Ej: Observaci&oacute;n Post-Quir&uacute;rgica / Tratamiento" required>
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
<!-- Modal Atender Cita (Smart UI) -->
<div class="modal fade" id="modalAtenderCita" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-heart-pulse-fill me-2 text-danger"></i>Consulta M&eacute;dica Avanzada - <span id="atenderCitaPaciente" class="text-info"></span></h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      
      <form action="adminAction" method="post" id="formAtenderCita">
        <input type="hidden" name="action" value="atenderCita">
        <input type="hidden" name="idCita" id="atenderIdCita">
        <input type="hidden" name="pacienteNombre" id="atenderPacNombre">
        
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
                            <input type="number" id="atender_fc_input" class="form-control" placeholder="Ej: 80" min="0" oninput="if(typeof formatearFC === 'function') formatearFC(this); if(typeof evaluarVitales === 'function') evaluarVitales();">
                            <div id="atender_fc_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary">Presi&oacute;n Arterial (Sist/Diast)</label>
                            <input type="text" id="atender_pa_input" class="form-control" placeholder="Ej: 120/80" onkeyup="if(typeof formatearPresion === 'function') formatearPresion(this);" oninput="if(typeof evaluarVitales === 'function') evaluarVitales();">
                            <div id="atender_pa_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary">Frecuencia Respiratoria</label>
                            <input type="number" id="atender_fr_input" class="form-control" placeholder="Ej: 16" min="0" oninput="if(typeof formatearFR === 'function') formatearFR(this); if(typeof evaluarVitales === 'function') evaluarVitales();">
                            <div id="atender_fr_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Saturaci&oacute;n O2 (%)</label>
                            <input type="number" id="atender_sat_input" class="form-control" placeholder="Ej: 98" min="0" oninput="if(typeof formatearSat === 'function') formatearSat(this); if(typeof evaluarVitales === 'function') evaluarVitales();">
                            <div id="atender_sat_badge" class="badge mt-1 w-100 p-2 text-wrap bg-secondary">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary">Temperatura (&deg;C)</label>
                            <input type="number" step="0.1" id="atender_temp_input" class="form-control" placeholder="Ej: 37.0" min="0" oninput="if(typeof formatearTemperatura === 'function') formatearTemperatura(this); if(typeof evaluarVitales === 'function') evaluarVitales();">
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
<!-- Modal Facturar Venta -->



<div class="modal fade" id="modalFacturarVenta" tabindex="-1" aria-hidden="true">

<div class="modal-dialog">

        

<div class="modal-content text-theme" style="background-color: #1a2235; border: 1px solid #2d3748; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">

            

<div class="modal-header border-0">

<h5 class="modal-title fw-bold">

<i class="bi bi-receipt me-2"></i>Facturaci&oacute;n de Venta de Farmacia</h5>

                <button type="button" class="btn-close btn-close-white" aria-label="Close" onclick="cerrarModalVenta()"></button>

            

</div>

<div class="modal-body">

<div class="mb-3">

                    <label class="form-label fw-semibold">Nombre del Cliente / Paciente</label>

                    <input type="text" id="ventaCliente" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" placeholder="Consumidor Final" required></div><div class="mb-3">

                    <label class="form-label fw-semibold">Medicamento a Vender</label>

                    <input type="text" id="ventaNombreMed" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" disabled>

</div>

<div class="row">

                    

<div class="col-md-6 mb-3">

                        <label class="form-label fw-semibold">Cantidad (Max: <span id="ventaMaxStock"></span>)</label>

                        <input type="number" id="ventaCantidad" class="form-control" style="background-color:#0b0f19; color:#fff; border:1px solid #374151;" min="1" value="1" oninput="calcTotalVenta()">

                    

</div>

<div class="col-md-6 mb-3">

                        <label class="form-label fw-semibold">Total a Pagar</label>

                        <input type="text" id="ventaTotal" class="form-control text-success fw-bold" style="background-color:#0b0f19; border:1px solid #374151;" disabled>

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

    <p style="text-align:center; font-size:12px; margin-top:0;">FACTURA DE VENTA ELECTRÃ“NICA</p>

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
      <form action="adminAction" method="POST">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="asignarEspecialidad">
          <input type="hidden" name="correo" id="espUserEmail">
          <p class="text-secondary small mb-3">Selecciona la especialidad médica para <span id="espUserDisplay" class="fw-bold text-theme"></span></p>
          <select name="nuevaEspecialidad" id="selectEspecialidadModal" class="form-select form-select-lg mb-3">
             <option value="Medicina General">Medicina General</option>
             <option value="Pediatría">Pediatría</option>
             <option value="Cardiología">Cardiología</option>
             <option value="Neurología">Neurología</option>
             <option value="Ginecología">Ginecología</option>
             <option value="Traumatología">Traumatología</option>
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

<!-- Modal Medicamento -->
<div class="modal fade" id="modalMedicamento" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-capsule me-2 text-success"></i>Registrar Nuevo Medicamento</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalMedicamento()"></button>
      </div>
      <form action="adminAction" method="POST">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="crearMedicamento">
          <div class="mb-3">
             <label class="form-label small text-secondary">Nombre Farmacológico</label>
             <input type="text" name="nombre" class="form-control" required>
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Presentación</label>
             <input type="text" name="presentacion" class="form-control" placeholder="Ej: Tabletas 500mg" required>
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Stock Inicial</label>
             <input type="number" name="stock" class="form-control" min="0" value="0" required>
          </div>
          <div class="mb-3">
             <label class="form-label small text-secondary">Precio Unitario ($)</label>
             <input type="number" name="precio" step="0.01" class="form-control" min="0" value="0.00" required>
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
<div class="modal fade" id="modalCatálogos" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold" id="catModalTitulo"><i class="bi bi-folder-plus me-2 text-info"></i>Nuevo Elemento de Catálogo</h5>
        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalCatálogos()"></button>
      </div>
      <form action="adminAction" method="POST">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" id="catActionInput" value="crearEnfermedad">
          <input type="hidden" name="id" id="catIdEnf">
          <input type="hidden" name="idAle" id="catIdAle">
          
          <div id="formEnfermedad" class="mb-3">
             <label class="form-label small text-secondary">Nombre de la Patología</label>
             <input type="text" name="nombreEnf" id="catNombreEnf" class="form-control">
             <label class="form-label small text-secondary mt-2">Descripción</label>
             <textarea name="descEnf" id="catDescEnf" class="form-control" rows="2"></textarea>
          </div>
          
          <div id="formAlergia" class="mb-3 d-none">
             <label class="form-label small text-secondary">Nombre del Alérgeno</label>
             <input type="text" name="nombreAle" id="catNombreAle" class="form-control">
             <label class="form-label small text-secondary mt-2">Gravedad</label>
             <select name="gravedadAle" id="catGravAle" class="form-select">
                <option value="Leve">Leve</option>
                <option value="Moderada">Moderada</option>
                <option value="Severa">Severa</option>
             </select>
          </div>
        </div>
        <div class="modal-footer border-0 pt-0 mt-3">
          <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalCatálogos()">Cancelar</button>
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
      <form action="agendarCita" method="POST" onsubmit="return validarCitaAdmin(event)">
        <div class="modal-body pb-0">
          <input type="hidden" name="action" value="crearCitaAdmin">
          <input type="hidden" id="citaEsNuevoPac" name="esNuevoPaciente" value="false">
          
          <div class="mb-3">
             <label class="form-label small text-secondary">C&eacute;dula del Paciente (10 d&iacute;gitos)</label>
             <input type="hidden" id="citaPacienteIdHidden" name="pacienteId">`n             <input type="text" id="citaCedula" name="cedula" class="form-control" placeholder="Ej: 0912345678" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, ''); buscarPacienteCita(this.value);" required>
             <div id="citaPacNombre" class="form-text text-info mt-1"></div>
          </div>
          
          <!-- QUICK REGISTER FALLBACK -->
          <div id="citaQuickRegister" class="d-none p-3 mb-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px dashed rgba(255,255,255,0.2);">
              <p class="small text-warning fw-bold mb-2"><i class="bi bi-exclamation-triangle me-1"></i>Paciente Nuevo. Complete datos:</p>
              <div class="row g-2">
                  <div class="col-md-6">
                      <input type="text" id="citaNombres" name="nuevoNombres" class="form-control form-control-sm" placeholder="Nombres completos">
                  </div>
                  <div class="col-md-6">
                      <input type="text" id="citaApellidos" name="nuevoApellidos" class="form-control form-control-sm" placeholder="Apellidos completos">
                  </div>
                  <div class="col-md-6">
                      <input type="date" id="citaFechaNac" name="nuevoFechaNac" class="form-control form-control-sm" title="Fecha de Nacimiento">
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
             <input type="datetime-local" id="citaFechaHora" name="fechaHora" class="form-control" required>
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