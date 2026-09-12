# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_script = '''
window.confirmarBorradoFactura = function(id) {
    Swal.fire({
        title: '\xbfEliminar Factura?',
        text: "Esta acci\xf3n es irreversible.",
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
            formData.append("action", "eliminarFactura");
            formData.append("id", id);
            fetch('adminAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminada', text: 'La factura ha sido eliminada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard";
                });
            });
        }
    });
};
'''

c = c + new_script

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added confirmarBorradoFactura")
