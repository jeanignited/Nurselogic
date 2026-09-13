# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

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

print("scripts.jsp injected print func.")
