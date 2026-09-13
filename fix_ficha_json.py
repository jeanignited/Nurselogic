import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old = '''document.getElementById('fichaInfo').innerText = 'C\u00E9dula: ' + data.cedula + ' | Nacimiento: ' + (data.fechaNacimiento || '--') + ' | Sexo: ' + (data.sexo || '--');
                document.getElementById('fichaFechaActualizacion').innerHTML = '<i class="bi bi-calendar3 me-1"></i> Fecha: ' + new Date().toLocaleDateString();
                document.getElementById('fichaEstPeso').innerText = (data.estatura || '--') + ' cm / ' + (data.peso || '--') + ' kg';
                document.getElementById('fichaTemp').innerText = (data.temperatura || '--') + ' \u00B0C';
                document.getElementById('fichaPresion').innerText = (data.presionArterial || '--');
                document.getElementById('fichaFcSat').innerText = (data.frecuenciaCardiaca || '--') + ' lpm / ' + (data.saturacionOxigeno || '--') + ' %';
                document.getElementById('fichaEnfermedades').innerText = data.enfermedades && data.enfermedades.length > 0 ? data.enfermedades : 'Ninguna registrada';
                document.getElementById('fichaAlergias').innerText = data.alergias && data.alergias.length > 0 ? data.alergias : 'Ninguna registrada';
                
                let container = document.getElementById('fichaAlertasContenedor');
                container.innerHTML = '';
                if (data.alergias && data.alergias.trim() !== '' && data.alergias.trim() !== 'Ninguna') {
                    container.innerHTML += '<div class="alert alert-danger py-2 mb-2 border-0" style="background: rgba(220,38,38,0.1);"><i class="bi bi-exclamation-octagon-fill me-2"></i>Paciente reporta alergias. Riesgo de shock anafil\u00E1ctico.</div>';
                }
                if (data.presionArterial) {
                    let parts = data.presionArterial.split('/');'''

new = '''document.getElementById('fichaInfo').innerText = 'C\u00E9dula: ' + cedula + ' | Nacimiento: ' + (data.fechaNacimiento || '--') + ' | Sexo: ' + (data.sexo || '--');
                document.getElementById('fichaFechaActualizacion').innerHTML = '<i class="bi bi-calendar3 me-1"></i> Fecha: ' + new Date().toLocaleDateString();
                document.getElementById('fichaEstPeso').innerText = (data.estatura && data.estatura !== '0.0' ? data.estatura : '--') + ' cm / ' + (data.peso && data.peso !== '0.0' ? data.peso : '--') + ' kg';
                document.getElementById('fichaTemp').innerText = (data.temperatura && data.temperatura !== '0.0' ? data.temperatura : '--') + ' \u00B0C';
                document.getElementById('fichaPresion').innerText = (data.presion && data.presion.trim() !== '' ? data.presion : '--');
                document.getElementById('fichaFcSat').innerText = (data.fc && data.fc !== 0 ? data.fc : '--') + ' lpm / ' + (data.sat && data.sat !== 0 ? data.sat : '--') + ' %';
                document.getElementById('fichaEnfermedades').innerText = data.enfermedad && data.enfermedad.length > 0 && data.enfermedad !== 'null' ? data.enfermedad : 'Ninguna registrada';
                document.getElementById('fichaAlergias').innerText = data.alergias && data.alergias.length > 0 && data.alergias !== 'null' ? data.alergias : 'Ninguna registrada';
                
                let container = document.getElementById('fichaAlertasContenedor');
                container.innerHTML = '';
                if (data.alergias && data.alergias.trim() !== '' && data.alergias.trim() !== 'Ninguna' && data.alergias.trim() !== 'null') {
                    container.innerHTML += '<div class="alert alert-danger py-2 mb-2 border-0" style="background: rgba(220,38,38,0.1);"><i class="bi bi-exclamation-octagon-fill me-2"></i>Paciente reporta alergias. Riesgo de shock anafil\u00E1ctico.</div>';
                }
                if (data.presion) {
                    let parts = data.presion.split('/');'''

c = c.replace(old, new)
with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Fixed ficha JSON mapping")
