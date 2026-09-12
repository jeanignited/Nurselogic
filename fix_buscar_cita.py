import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_func = '''window.buscarPacienteCita = function(cedula) {
    const infoDiv = document.getElementById('citaPacNombre');
    const quickReg = document.getElementById('citaQuickRegister');
    const esNuevo = document.getElementById('citaEsNuevoPac');
    const btn = document.getElementById('btnAgendarCita');
    
    if (cedula.length === 10) {
        if (infoDiv) infoDiv.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Buscando...';
        if (btn) btn.disabled = true;
        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if (data.id) {
                    if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + data.nombres + ' ' + data.apellidos;
                    if (quickReg) quickReg.classList.add('d-none');
                    if (esNuevo) esNuevo.value = "false";
                    var hiddenId = document.getElementById('citaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = data.id;
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('citaNombres'); if (nN) nN.required = false;
                    var nA = document.getElementById('citaApellidos'); if (nA) nA.required = false;
                } else {
                    if (infoDiv) infoDiv.innerHTML = '';
                    if (quickReg) quickReg.classList.remove('d-none');
                    if (esNuevo) esNuevo.value = "true";
                    var hiddenId = document.getElementById('citaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = "";
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('citaNombres'); if (nN) nN.required = true;
                    var nA = document.getElementById('citaApellidos'); if (nA) nA.required = true;
                }
            }).catch(e => {
                if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-exclamation-triangle-fill text-danger me-1"></i> Error de conexi\xf3n.';
            });
    } else {
        if (infoDiv) infoDiv.innerHTML = '';
        if (quickReg) quickReg.classList.add('d-none');
        if (esNuevo) esNuevo.value = "false";
        if (btn) btn.disabled = false;
    }
};
'''

c = c.replace('window.buscarPacienteCama = function(cedula) {', new_func + '\nwindow.buscarPacienteCama = function(cedula) {')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added buscarPacienteCita")
