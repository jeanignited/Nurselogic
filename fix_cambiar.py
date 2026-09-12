import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_func = r"function cambiarEstadoCita\(idCita, nuevoEstado\)\s*\{\s*document\.getElementById\('adminActionType'\)\.value = 'actualizarEstadoCita';\s*document\.getElementById\('adminActionTarget'\)\.value = 'cita';\s*document\.getElementById\('adminActionId'\)\.value = idCita;\s*let inputEst = document\.getElementById\('adminActionNuevoEst'\);\s*if \(!inputEst\)\s*\{\s*inputEst = document\.createElement\('input'\);\s*inputEst\.type = 'hidden';\s*inputEst\.name = 'nuevoEstado';\s*inputEst\.id = 'adminActionNuevoEst';\s*document\.getElementById\('formAdminAction'\)\.appendChild\(inputEst\);\s*\}\s*inputEst\.value = nuevoEstado;\s*document\.getElementById\('formAdminAction'\)\.submit\(\);\s*\}"

new_func = '''function cambiarEstadoCita(idCita, nuevoEstado) {
            let executeChange = () => {
                var formData = new URLSearchParams();
                formData.append("action", "actualizarEstadoCita");
                formData.append("target", "cita");
                formData.append("id", idCita);
                formData.append("nuevoEstado", nuevoEstado);
                fetch('adminAction', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: formData.toString()
                }).then(function(response) {
                    Swal.fire({title: 'Actualizado', text: 'El estado de la cita ha sido actualizado a ' + nuevoEstado, icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                        window.location.href = "dashboard";
                    });
                });
            };

            if (nuevoEstado === 'CANCELADO') {
                Swal.fire({
                    title: '\xbfCancelar Cita?',
                    text: '\xbfEst\xe1s seguro de que deseas cancelar esta cita? Esta acci\xf3n la mover\xe1 al historial de cancelados.',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#3085d6',
                    confirmButtonText: 'S\xed, Cancelar',
                    cancelButtonText: 'No, mantener',
                    background: 'var(--bg-panel)',
                    color: 'var(--text-color)'
                }).then((result) => {
                    if (result.isConfirmed) {
                        executeChange();
                    }
                });
            } else {
                executeChange();
            }
        }'''

c = re.sub(old_func, new_func, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated cambiarEstadoCita")
