import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx1 = c.find('function borrarCatalogo(tipo, id, nombre)')
idx2 = c.find('}', idx1)
while True:
    if c[idx2+1:idx2+20].strip() == 'function':
        break
    idx2 = c.find('}', idx2+1)
    if idx2 == -1:
        break

old_cat = c[idx1:idx2+1]

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

c = c.replace(old_cat, new_cat)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced borrarCatalogo")
