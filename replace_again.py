import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will replace the whole block again properly!
m = re.search(r"let diagStr = .*?document\.getElementById\('fichaReceta'\)\.innerText = recStr;\s*\}", c, re.DOTALL)
if m:
    new_code = '''let diagStr = (data.diagnosticoClinico && data.diagnosticoClinico !== 'null' && data.diagnosticoClinico.trim() !== '') ? data.diagnosticoClinico : 'No registrado';
                if (diagStr.length > 80 && diagStr !== 'No registrado') {
                    let safeDiag = diagStr.replace(/'/g, "\\\\'").replace(/\\r?\\n/g, "<br>").replace(/\"/g, "&quot;");
                    let btn = '<button class="btn btn-sm btn-outline-info ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: \\'Diagn\u00F3stico\\', html: \\'' + safeDiag + '\\', background: \\'var(--bg-panel)\\', color: \\'var(--text-color)\\'})">Ver detalles</button>';
                    document.getElementById('fichaDiagnostico').innerHTML = diagStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaDiagnostico').innerText = diagStr;
                }

                let recStr = (data.receta && data.receta !== 'null' && data.receta.trim() !== '') ? data.receta : 'No registrado';
                if (recStr.length > 80 && recStr !== 'No registrado') {
                    let safeRec = recStr.replace(/'/g, "\\\\'").replace(/\\r?\\n/g, "<br>").replace(/\"/g, "&quot;");
                    let btn = '<button class="btn btn-sm btn-outline-success ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: \\'Receta M\u00E9dica\\', html: \\'' + safeRec + '\\', background: \\'var(--bg-panel)\\', color: \\'var(--text-color)\\'})">Ver detalles</button>';
                    document.getElementById('fichaReceta').innerHTML = recStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaReceta').innerText = recStr;
                }'''
    c = c.replace(m.group(0), new_code)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced completely")
else:
    print("Not found")
