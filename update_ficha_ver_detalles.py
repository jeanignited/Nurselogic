import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_diag_receta = '''                document.getElementById('fichaDiagnostico').innerText = (data.diagnosticoClinico && data.diagnosticoClinico !== 'null' && data.diagnosticoClinico.trim() !== '') ? data.diagnosticoClinico : 'No registrado';
                document.getElementById('fichaReceta').innerText = (data.receta && data.receta !== 'null' && data.receta.trim() !== '') ? data.receta : 'No registrado';'''

new_diag_receta = '''                let diagStr = (data.diagnosticoClinico && data.diagnosticoClinico !== 'null' && data.diagnosticoClinico.trim() !== '') ? data.diagnosticoClinico : 'No registrado';
                if (diagStr.length > 80 && diagStr !== 'No registrado') {
                    let btn = <button class="btn btn-sm btn-outline-info ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: 'Diagn&oacute;stico', text: \${diagStr.replace(//g, "'")}\, background: 'var(--bg-panel)', color: 'var(--text-color)'})">Ver detalles</button>;
                    document.getElementById('fichaDiagnostico').innerHTML = diagStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaDiagnostico').innerText = diagStr;
                }

                let recStr = (data.receta && data.receta !== 'null' && data.receta.trim() !== '') ? data.receta : 'No registrado';
                if (recStr.length > 80 && recStr !== 'No registrado') {
                    let btn = <button class="btn btn-sm btn-outline-success ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: 'Receta M&eacute;dica', text: \${recStr.replace(//g, "'")}\, background: 'var(--bg-panel)', color: 'var(--text-color)'})">Ver detalles</button>;
                    document.getElementById('fichaReceta').innerHTML = recStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaReceta').innerText = recStr;
                }'''

c = c.replace(old_diag_receta, new_diag_receta)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
