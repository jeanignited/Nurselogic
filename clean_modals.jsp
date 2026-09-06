<!-- Modal Cambio de Rol -->
        <div class="modal fade" id="modalRol" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content text-white" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
                    <div class="modal-header border-0">
                        <h5 class="modal-title fw-bold"><i class="bi bi-shield-lock me-2 text-primary"></i>Cambiar Rol de Usuario</h5>
                        <button type="button" class="btn-close btn-close-white" onclick="cerrarModalRol()"></button>
                    </div>
                    <div class="modal-body pb-0">
                        <p class="text-secondary small mb-3">Selecciona el nuevo nivel de acceso para <span id="rolUserEmail" class="fw-bold text-white"></span></p>
                        <select id="rolSelectModal" class="form-select form-select-lg mb-3">
                            <option value="Admin">Admin</option>
                            <option value="Medico">Medico</option>
                            <option value="Paciente">Paciente</option>
                            <option value="Pendiente">Pendiente</option>
                        </select>
                    </div>
                    <div class="modal-footer border-0 pt-0">
                        <button type="button" class="btn btn-secondary px-4" onclick="cerrarModalRol()">Cancelar</button>
                        <button type="button" class="btn btn-primary px-4" onclick="guardarCambioRol()">Guardar Cambios</button>
                    </div>
                </div>
            </div>
        </div>","StartLine":430,"TargetContent":"        <form id="formAdminAction" action="adminAction" method="POST" style="display:none;">
            <input type="hidden" name="action" id="adminActionType">
            <input type="hidden" name="tipo" id="adminActionTarget">
            <input type="hidden" name="id" id="adminActionId">
            <input type="hidden" name="nuevoRol" id="adminActionRol">
        </form>"},{"AllowMultiple":false,"EndLine":817,"ReplacementContent":"        function abrirModalRol(correo, rolActual) {
            document.getElementById('rolUserEmail').innerText = correo;
            document.getElementById('rolSelectModal').value = rolActual;
            document.getElementById('modalRol').classList.add('show');
            document.getElementById('modalRol').style.display = 'block';
            document.getElementById('modalRol').style.backgroundColor = 'rgba(0,0,0,0.5)';
        }

        function cerrarModalRol() {
            document.getElementById('modalRol').classList.remove('show');
            document.getElementById('modalRol').style.display = 'none';
        }

        function guardarCambioRol() {
            let correo = document.getElementById('rolUserEmail').innerText;
            let nuevoRol = document.getElementById('rolSelectModal').value;
            
            document.getElementById('adminActionType').value = 'editarRol';
            document.getElementById('adminActionTarget').value = 'usuario';
            document.getElementById('adminActionId').value = correo;
            document.getElementById('adminActionRol').value = nuevoRol;
            document.getElementById('formAdminAction').submit();
        }
    </script>
</body>","StartLine":806,"TargetContent":"        function editarRolUsuario(correo, rolActual) {
            let opciones = "Roles disponibles:\
- Admin\
- Medico\
- Pendiente\
\
Rol actual: " + rolActual + "\
\
Ingresa el nuevo rol:";
            let nuevoRol = prompt(opciones, rolActual);
            if (nuevoRol != null && nuevoRol.trim() !== "" && nuevoRol.trim() !== rolActual) {
                document.getElementById('adminActionType').value = 'editarRol';
                document.getElementById('adminActionTarget').value = 'usuario';
                document.getElementById('adminActionId').value = correo;
                document.getElementById('adminActionRol').value = nuevoRol.trim();
                document.getElementById('formAdminAction').submit();
            }
        }
    </script>
</body>"}],"TargetFile":"C:\Users\THINKPAD\IdeaProjects\
urselogic-web\src\main\webapp\index.jsp","toolAction":"Modify index.jsp to use a modal","toolSummary":"Update index.jsp"}}]}
