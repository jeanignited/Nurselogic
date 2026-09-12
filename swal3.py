# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

c = re.sub(r'window\.confirmarAltaCama = function\(id, numero, paciente\) \{.*?\}\n\};', 
'''window.confirmarAltaCama = function(id, numero, paciente) {
    Swal.fire({
        title: 'Dar de Alta',
        text: "\xbfConfirmas dar de alta a " + paciente + " y liberar la " + numero + "?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'S\xed, Dar de Alta',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "liberar");
            formData.append("camaId", id);
            fetch('camasAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Alta confirmada', text: 'La ' + numero + ' ha sido liberada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.reload();
                });
            });
        }
    });
};''', c, flags=re.DOTALL)

c = re.sub(r'window\.confirmarBorradoCama = function\(id, numero\) \{.*?\}\n\};', 
'''window.confirmarBorradoCama = function(id, numero) {
    Swal.fire({
        title: '\xbfEliminar Cama?',
        text: "\xbfEst\xe1s seguro de eliminar la " + (numero || "cama seleccionada") + "? Esta acci\xf3n es irreversible.",
        icon: 'error',
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
            formData.append("camaId", id);
            fetch('camasAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminada', text: 'La cama ha sido eliminada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.reload();
                });
            });
        }
    });
};''', c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced!")
