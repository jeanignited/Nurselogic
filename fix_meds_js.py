import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = '''
window.borrarMedicamento = function(id) {
    Swal.fire({
        title: 'Eliminar F\\u00E1rmaco?',
        text: "Esta acci\\u00F3n es irreversible.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'S\\u00ED, Eliminar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "eliminarMedicamento");
            formData.append("id", id);
            fetch('adminAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminado', text: 'El f\\u00E1rmaco ha sido eliminado.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard?vista=medicamentos";
                });
            });
        }
    });
};
'''

c = c.replace('window.confirmarBorradoFactura = function(id) {', new_js + '\nwindow.confirmarBorradoFactura = function(id) {')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added borrarMedicamento JS")
