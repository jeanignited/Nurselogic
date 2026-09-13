# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_logic = '''let formattedDiag = rawDiag.replace(/(FC:|PA:|FR:|Temp:|IMC:|Glasgow:|SpO2:|Talla:|Peso:)\\s*([^\\n]+)/gi, '<span class="badge bg-secondary me-2 mb-2 px-3 py-2" style="font-size: 0.85rem;"><i class="bi bi-activity text-info me-1"></i> </span>');
    formattedDiag = formattedDiag.replace(/\\n/g, '<br>');
    document.getElementById('verDiagTexto').innerHTML = '<div class="card bg-dark border-secondary p-3 text-light" style="line-height: 1.8;">' + formattedDiag + '</div>';'''

new_logic = '''let cleanDiag = rawDiag.replace(/Â°C/g, '°C');
    let vitalSignsHtml = '';
    let restText = cleanDiag;
    
    let regex = /(FC:|PA:|FR:|Temp:|IMC:|Glasgow:|SpO2:|Talla:|Peso:)\\s*([^\\n]+)\\n?/gi;
    let match;
    while ((match = regex.exec(cleanDiag)) !== null) {
         vitalSignsHtml += '<div class="col-md-4 col-6 mb-2"><i class="bi bi-activity text-info me-1"></i><span class="text-light fw-semibold">' + match[1] + '</span> <span class="text-light opacity-75">' + match[2] + '</span></div>';
         restText = restText.replace(match[0], '');
    }
    
    let finalHtml = '';
    if (vitalSignsHtml !== '') {
         finalHtml += '<div class="row mb-3">' + vitalSignsHtml + '</div><hr class="border-secondary opacity-25">';
    }
    finalHtml += restText.replace(/\\n/g, '<br>');
    document.getElementById('verDiagTexto').innerHTML = '<div class="card bg-dark border-secondary p-3 text-light" style="line-height: 1.8;">' + finalHtml + '</div>';'''

c = c.replace(old_logic, new_logic)

imprimir_func = '''
function imprimirHistorialMedico() {
    let modalBody = document.querySelector('#modalVerDiagnostico .modal-body');
    let contenido = modalBody ? modalBody.innerHTML : '';
    let ventana = window.open('', '', 'width=800,height=600');
    ventana.document.write('<html><head><title>Historial Clínico</title>');
    ventana.document.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">');
    ventana.document.write('</head><body><div class="container mt-4">');
    ventana.document.write('<h2>Historial Clínico del Paciente</h2><hr>');
    ventana.document.write(contenido.replace(/Â°C/g, '°C'));
    ventana.document.write('</div></body></html>');
    ventana.document.close();
    setTimeout(() => { ventana.print(); ventana.close(); }, 500);
}
</script>'''

# Replace the last </script>
idx = c.rfind('</script>')
if idx != -1:
    c = c[:idx] + imprimir_func + c[idx+9:]

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("scripts.jsp logic replaced successfully.")
