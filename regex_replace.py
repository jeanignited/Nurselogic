import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. confirmarBorrado
old_borrado = r"function confirmarBorrado\(tipo, id\)\s*\{\s*if\s*\(confirm\('[^']+' \+ tipo \+ '[^']+'\)\)\s*\{\s*document\.getElementById\('adminActionType'\)\.value = 'eliminar';\s*document\.getElementById\('adminActionTarget'\)\.value = tipo;\s*document\.getElementById\('adminActionId'\)\.value = id;\s*document\.getElementById\('formAdminAction'\)\.submit\(\);\s*\}\s*\}"
new_borrado = '''function confirmarBorrado(tipo, id) {
            Swal.fire({
                title: '\xbfEliminar ' + tipo + '?',
                text: 'Esta acci\xf3n no se puede deshacer.',
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
                    formData.append("action", "eliminar");
                    formData.append("target", tipo);
                    formData.append("id", id);
                    fetch('adminAction', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: formData.toString()
                    }).then(function(response) {
                        Swal.fire({title: 'Eliminado', text: 'El registro ha sido eliminado exitosamente.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                            window.location.href = "dashboard";
                        });
                    });
                }
            });
        }'''
c = re.sub(old_borrado, new_borrado, c, flags=re.DOTALL)

# 2. confirmarEliminarCatalogo
old_cat = r"function confirmarEliminarCatalogo\(id, tipo, nombre\)\s*\{\s*if\s*\(confirm\('[^']+' \+ nombre \+ '[^']+'\)\)\s*\{\s*document\.getElementById\('catActionType'\)\.value = 'eliminar';\s*document\.getElementById\('catActionTipoCat'\)\.value = tipo;\s*document\.getElementById\('catActionId'\)\.value = id;\s*document\.getElementById\('formCatalogoAction'\)\.submit\(\);\s*\}\s*\}"
new_cat = '''function confirmarEliminarCatalogo(id, tipo, nombre) {
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
                    formData.append("action", "eliminar");
                    formData.append("tipoCat", tipo);
                    formData.append("id", id);
                    fetch('catalogosAction', {
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

# 3. simple alerts
def replace_alert(match):
    msg = match.group(1)
    return "Swal.fire({text: " + msg + ", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'})"

c = re.sub(r'alert\((.*?)\)', replace_alert, c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced all with regex!")
