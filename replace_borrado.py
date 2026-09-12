import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. confirmarBorrado
old_borrado = '''        function confirmarBorrado(tipo, id) {
            if(confirm(' \xbfEstas seguro de que deseas eliminar este ' + tipo + '? Esta acci\xf3n no se puede deshacer.')) {
                document.getElementById('adminActionType').value = 'eliminar';
                document.getElementById('adminActionTarget').value = tipo;
                document.getElementById('adminActionId').value = id;
                document.getElementById('formAdminAction').submit();
            }
        }'''
new_borrado = '''        function confirmarBorrado(tipo, id) {
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
c = c.replace(old_borrado, new_borrado)

# 2. confirmarEliminarCatalogo
old_cat = '''        function confirmarEliminarCatalogo(id, tipo, nombre) {
            if (confirm('\xbfEst\xe1s seguro de eliminar "' + nombre + '" del cat\xe1logo cl\xednico?')) {
                document.getElementById('catActionType').value = 'eliminar';
                document.getElementById('catActionTipoCat').value = tipo;
                document.getElementById('catActionId').value = id;
                document.getElementById('formCatalogoAction').submit();
            }
        }'''
new_cat = '''        function confirmarEliminarCatalogo(id, tipo, nombre) {
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
c = c.replace(old_cat, new_cat)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced borrado & catalogo")
