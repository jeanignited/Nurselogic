import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r"let vitalesStr = '\\n--- Signos Vitales ---\\n' \+.*?glasgowTotal'\)\.innerText;", c, re.DOTALL)
if m:
    new_vitales = '''let talla = document.getElementById('atender_estatura_input') ? document.getElementById('atender_estatura_input').value : '';
    let peso = document.getElementById('atender_peso_input') ? document.getElementById('atender_peso_input').value : '';
    let imcValue = document.getElementById('atender_imcValor') ? document.getElementById('atender_imcValor').innerText : '0.0';
    let imcState = document.getElementById('atender_imcEstado') ? document.getElementById('atender_imcEstado').innerText : '';
    
    let vitalesStr = '\\n--- Signos Vitales ---\\n' +
        'Talla: ' + (talla ? talla + ' m' : 'No reg.') + '\\n' +
        'Peso: ' + (peso ? peso + ' kg' : 'No reg.') + '\\n' +
        'IMC: ' + imcValue + ' (' + imcState + ')\\n' +
        'FC: ' + document.getElementById('atender_fc_input').value + ' lpm\\n' +
        'PA: ' + document.getElementById('atender_pa_input').value + '\\n' +
        'FR: ' + document.getElementById('atender_fr_input').value + ' rpm\\n' +
        'SatO2: ' + document.getElementById('atender_sat_input').value + '%\\n' +
        'Temp: ' + document.getElementById('atender_temp_input').value + ' C\\n' +
        'Glasgow: ' + document.getElementById('glasgowTotal').innerText;'''
    c = c.replace(m.group(0), new_vitales)
    
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Success")
else:
    print("Not found")
