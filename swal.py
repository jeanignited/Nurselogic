import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace confirmarAltaCama
old_alta = '''window.confirmarAltaCama = function(id, numero, paciente) {
    if (confirm("SISTEMA ACTIVO: \xbfConfirmas dar de alta a " + paciente + " y liberar la " + numero + "?")) {
        var formData = new URLSearchParams();
        formData.append("action", "liberar");
        formData.append("camaId", id);
        fetch('camasAction', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData.toString()
        }).then(function(response) {
            alert("\xbfAlta confirmada! La " + numero + " ha sido liberada.");
            window.location.href = "dashboard";
        });
    }
};'''
new_alta = '''window.confirmarAltaCama = function(id, numero, paciente) {
    Swal.fire({
        title: 'Dar de Alta',
        text: "\xbfConfirmas dar de alta a " + paciente + " y liberar la " + numero + "?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'S, Dar de Alta',
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
                    window.location.href = "dashboard";
                });
            });
        }
    });
};'''
c = c.replace(old_alta, new_alta)

# Replace confirmarBorradoCama
old_borrado_cama = '''window.confirmarBorradoCama = function(id, numero) {
    if (confirm("\xbfEst\xe1s seguro de que deseas eliminar la " + (numero || "cama seleccionada") + "? Esta acci\xf3n no se puede deshacer.")) {
        var formData = new URLSearchParams();
        formData.append("action", "eliminar");
        formData.append("camaId", id);
        fetch('camasAction', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData.toString()
        }).then(function(response) {
            alert("La cama ha sido eliminada del sistema.");
            window.location.href = "dashboard";
        }).catch(function(err) {
            alert("Error al eliminar la cama.");
        });
    }
};'''
new_borrado_cama = '''window.confirmarBorradoCama = function(id, numero) {
    Swal.fire({
        title: '\xbfEliminar Cama?',
        text: "\xbfEst\xe1s seguro de eliminar la " + (numero || "cama seleccionada") + "? Esta acci\xf3n es irreversible.",
        icon: 'error',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'S, Eliminar',
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
                    window.location.href = "dashboard";
                });
            });
        }
    });
};'''
c = c.replace(old_borrado_cama, new_borrado_cama)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Swal added to Cama functions")
