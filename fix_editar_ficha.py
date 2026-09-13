import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = '''
window.editarPacienteDesdeFicha = function() {
    let cedulaText = document.getElementById('fichaInfo').innerText;
    let match = cedulaText.match(/C\u00E9dula: (\d+)/);
    if (match && match[1]) {
        cerrarModalFicha();
        editarPaciente(match[1]);
    } else {
        Swal.fire('Error', 'No se pudo obtener la c\u00E9dula del paciente.', 'error');
    }
};
'''

c = c.replace('window.cerrarModalFicha = function() {', new_js + '\nwindow.cerrarModalFicha = function() {')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Added editarPacienteDesdeFicha")
