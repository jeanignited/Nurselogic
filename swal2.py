import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace confirmarAltaCama
c = re.sub(r'window\.confirmarAltaCama = function\(id, numero, paciente\) \{.*?\}\n\};', 
'''window.confirmarAltaCama = function(id, numero, paciente) {
    Swal.fire({
        title: 'Dar de Alta',
        text: "¿Confirmas dar de alta a " + paciente + " y liberar la " + numero + "?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Dar de Alta',
        cancelButtonText: 'Cancelar'
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
                Swal.fire('Alta confirmada', 'La ' + numero + ' ha sido liberada.', 'success').then(() => {
                    window.location.reload();
                });
            });
        }
    });
};''', c, flags=re.DOTALL)

# Replace confirmarBorradoCama
c = re.sub(r'window\.confirmarBorradoCama = function\(id, numero\) \{.*?\}\n\};', 
'''window.confirmarBorradoCama = function(id, numero) {
    Swal.fire({
        title: '¿Eliminar Cama?',
        text: "¿Estás seguro de eliminar la " + (numero || "cama seleccionada") + "? Esta acción es irreversible.",
        icon: 'error',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, Eliminar',
        cancelButtonText: 'Cancelar'
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
                Swal.fire('Eliminada', 'La cama ha sido eliminada.', 'success').then(() => {
                    window.location.reload();
                });
            });
        }
    });
};''', c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced!")
