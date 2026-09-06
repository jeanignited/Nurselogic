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
                            <div class="p-2 border rounded text-center plantilla-card" style="border-color: rgba(255,255,255,0.2) !important; cursor: pointer; background: rgba(255,255,255,0.05);" onclick="aplicarPlantillaRol('Medico', this)">
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
                                    <input class="form-check-input perm-checkbox" type="checkbox" name="permisos" value="Catalogos">
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