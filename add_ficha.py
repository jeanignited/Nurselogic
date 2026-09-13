import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = '''
window.verFichaClinica = function(cedula) {
    if (!cedula) return;
    Swal.fire({title: 'Cargando Ficha...', text: 'Obteniendo informaci\u00F3n del paciente...', allowOutsideClick: false, didOpen: () => { Swal.showLoading(); }});
    fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
        .then(r => r.json())
        .then(data => {
            Swal.close();
            if (data.id) {
                document.getElementById('fichaNombre').innerText = data.nombres + ' ' + data.apellidos;
                document.getElementById('fichaInfo').innerText = 'C\u00E9dula: ' + data.cedula + ' | Nacimiento: ' + (data.fechaNacimiento || '--') + ' | Sexo: ' + (data.sexo || '--');
                document.getElementById('fichaFechaActualizacion').innerHTML = '<i class="bi bi-calendar3 me-1"></i> Fecha: ' + new Date().toLocaleDateString();
                document.getElementById('fichaEstPeso').innerText = (data.estatura || '--') + ' cm / ' + (data.peso || '--') + ' kg';
                document.getElementById('fichaTemp').innerText = (data.temperatura || '--') + ' \u00B0C';
                document.getElementById('fichaPresion').innerText = (data.presionArterial || '--');
                document.getElementById('fichaFcSat').innerText = (data.frecuenciaCardiaca || '--') + ' lpm / ' + (data.saturacionOxigeno || '--') + ' %';
                document.getElementById('fichaEnfermedades').innerText = data.enfermedades && data.enfermedades.length > 0 ? data.enfermedades : 'Ninguna registrada';
                document.getElementById('fichaAlergias').innerText = data.alergias && data.alergias.length > 0 ? data.alergias : 'Ninguna registrada';
                
                let container = document.getElementById('fichaAlertasContenedor');
                container.innerHTML = '';
                if (data.alergias && data.alergias.trim() !== '') {
                    container.innerHTML += '<div class="alert alert-danger py-2 mb-2 border-0" style="background: rgba(220,38,38,0.1);"><i class="bi bi-exclamation-octagon-fill me-2"></i>Paciente reporta alergias. Riesgo de shock anafil\u00E1ctico.</div>';
                }
                if (data.presionArterial) {
                    let parts = data.presionArterial.split('/');
                    if (parts.length === 2 && parseInt(parts[0]) >= 140) {
                        container.innerHTML += '<div class="alert alert-warning py-2 mb-2 border-0" style="background: rgba(245,158,11,0.1);"><i class="bi bi-heart-pulse-fill me-2"></i>Hipertensi\u00F3n detectada. Monitorear signos vitales.</div>';
                    }
                }
                if (container.innerHTML === '') {
                    container.innerHTML = '<div class="alert alert-success py-2 mb-0 border-0" style="background: rgba(16,185,129,0.1);"><i class="bi bi-check-circle-fill me-2"></i>Par\u00E1metros estables. Ninguna alerta cl\u00EDnica urgente.</div>';
                }
                
                var mEl = document.getElementById('modalFichaClinica');
                if (mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }
            } else {
                Swal.fire('Error', 'Paciente no encontrado.', 'error');
            }
        })
        .catch(e => {
            Swal.fire('Error', 'Problema de conexi\u00F3n al cargar la ficha.', 'error');
        });
};

window.cerrarModalFicha = function() {
    var mEl = document.getElementById('modalFichaClinica');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }
};
'''

c = c.replace('// Inicializar estado del dropdown si es que existe', new_js + '\n// Inicializar estado del dropdown si es que existe')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added verFichaClinica to scripts.jsp")
