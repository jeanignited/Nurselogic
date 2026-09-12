import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_cat = r"function borrarCatalogo\(tipo, id, nombre\)\s*\{\s*if\s*\(confirm\('[^']+' \+ nombre \+ '[^']+'\)\)\s*\{\s*let f = document\.getElementById\('formAdminAction'\);\s*document\.getElementById\('adminActionType'\)\.value = tipo === 'enfermedad' \? 'borrarEnfermedad' : 'borrarAlergia';\s*let inputId = document\.createElement\('input'\);\s*inputId\.type = 'hidden';\s*inputId\.name = 'id';\s*inputId\.value = id;\s*f\.appendChild\(inputId\);\s*f\.submit\(\);\s*\}\s*\}"

new_cat = '''function borrarCatalogo(tipo, id, nombre) {
            Swal.fire({
                title: '\xbfEliminar del cat\xe1logo?',
                text: '\xbfEst\xe1s seguro de eliminar "' + nombre + '" del cat\xe1logo cl\xednico?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'S\xed, Eliminar',
                cancelButtonText: 'Cancelar',
                background: 'var(--bg-panel)',
                color: 'var(--text-color)'
            }).then((result) => {
                if (result.isConfirmed) {
                    var formData = new URLSearchParams();
                    formData.append("action", tipo === 'enfermedad' ? 'borrarEnfermedad' : 'borrarAlergia');
                    formData.append("id", id);
                    fetch('adminAction', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: formData.toString()
                    }).then(function(response) {
                        Swal.fire({title: 'Eliminado', text: 'El elemento ha sido eliminado.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                            window.location.href = "dashboard";
                        });
                    });
                }
            });
        }'''

c = re.sub(old_cat, new_cat, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
