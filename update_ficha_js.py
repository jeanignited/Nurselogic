import io
import re
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r"document\.getElementById\('fichaEstPeso'\)\.innerText = data\.estatura.*?;\n", c, re.DOTALL)
if m:
    new_script = '''document.getElementById('fichaEstPeso').innerText = data.estatura + ' m / ' + data.peso + ' kg';
                  let imc = (data.peso > 0 && data.estatura > 0) ? (data.peso / (data.estatura * data.estatura)).toFixed(1) : 0;
                  let imcBadge = document.getElementById('fichaIMC');
                  if(imc > 0) {
                      let estado = 'Normal'; let bg = 'bg-success';
                      if(imc < 18.5) { estado = 'Bajo peso'; bg = 'bg-warning'; }
                      else if(imc >= 25 && imc < 30) { estado = 'Sobrepeso'; bg = 'bg-warning'; }
                      else if(imc >= 30) { estado = 'Obesidad'; bg = 'bg-danger'; }
                      imcBadge.className = 'badge ms-2 ' + bg;
                      imcBadge.innerText = 'IMC: ' + imc + ' (' + estado + ')';
                  } else {
                      imcBadge.className = 'badge ms-2 bg-secondary';
                      imcBadge.innerText = 'IMC: Sin datos';
                  }
                  
                  let glasgowTd = document.getElementById('fichaGlasgow');
                  if(data.glasgow && data.glasgow !== 'null') {
                      glasgowTd.innerHTML = data.glasgow + ' / 15';
                  } else {
                      glasgowTd.innerHTML = '<span class="text-muted fst-italic">No se consider\u00F3 la evaluaci\u00F3n Glasgow</span>';
                  }
'''
    c = c.replace(m.group(0), new_script)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
