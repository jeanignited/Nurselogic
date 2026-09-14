import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r"document\.getElementById\('fichaDiagnostico'\)\.innerText = [^\n]*?;\n\s*document\.getElementById\('fichaReceta'\)\.innerText = [^\n]*?;", c)
if m:
    new_diag_receta = '''let diagStr = (data.diagnosticoClinico && data.diagnosticoClinico !== 'null' && data.diagnosticoClinico.trim() !== '') ? data.diagnosticoClinico : 'No registrado';
                if (diagStr.length > 80 && diagStr !== 'No registrado') {
                    let safeDiag = diagStr.replace(/'/g, "\\\\'");
                    let btn = '<button class="btn btn-sm btn-outline-info ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: \\'Diagn\\u00F3stico\\', text: \\'' + safeDiag + '\\', background: \\'var(--bg-panel)\\', color: \\'var(--text-color)\\'})">Ver detalles</button>';
                    document.getElementById('fichaDiagnostico').innerHTML = diagStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaDiagnostico').innerText = diagStr;
                }

                let recStr = (data.receta && data.receta !== 'null' && data.receta.trim() !== '') ? data.receta : 'No registrado';
                if (recStr.length > 80 && recStr !== 'No registrado') {
                    let safeRec = recStr.replace(/'/g, "\\\\'");
                    let btn = '<button class="btn btn-sm btn-outline-success ms-2 py-0" style="font-size: 0.75rem;" onclick="Swal.fire({title: \\'Receta\\', text: \\'' + safeRec + '\\', background: \\'var(--bg-panel)\\', color: \\'var(--text-color)\\'})">Ver detalles</button>';
                    document.getElementById('fichaReceta').innerHTML = recStr.substring(0, 80) + '...' + btn;
                } else {
                    document.getElementById('fichaReceta').innerText = recStr;
                }'''
    c = c.replace(m.group(0), new_diag_receta)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Success")
else:
    print("Not found")
