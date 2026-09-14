import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r"document\.getElementById\('fichaEstPeso'\)\.innerText = [^\n]+;", c)
if m:
    old_code = m.group(0)
    new_code = '''let estFicha = (data.estatura && data.estatura !== '0.0' && data.estatura !== '0') ? parseFloat(data.estatura) : null;
                let pesoFicha = (data.peso && data.peso !== '0.0' && data.peso !== '0') ? parseFloat(data.peso) : null;
                let imcTextFicha = '';
                if (estFicha && pesoFicha) {
                    let imcCalc = (pesoFicha / (estFicha * estFicha)).toFixed(1);
                    let st = imcCalc < 18.5 ? 'Bajo' : imcCalc < 25 ? 'Normal' : imcCalc < 30 ? 'Sobrepeso' : 'Obesidad';
                    imcTextFicha = ' <span class=\"badge bg-secondary ms-2\">IMC: ' + imcCalc + ' (' + st + ')</span>';
                }
                document.getElementById('fichaEstPeso').innerHTML = (estFicha ? estFicha : '--') + ' m / ' + (pesoFicha ? pesoFicha : '--') + ' kg' + imcTextFicha;'''
    c = c.replace(old_code, new_code)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced fichaEstPeso")
else:
    print("Not found")
