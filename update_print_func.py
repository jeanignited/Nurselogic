import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_func = re.search(r'function imprimirHistorialMedico\(\) \{[\s\S]*?setTimeout[\s\S]*?\}', c)

new_func = r'''function imprimirHistorialMedico(modalId = '#modalVerDiagnostico') {
    let modalBody = document.querySelector(modalId + ' .modal-body');
    let contenido = modalBody ? modalBody.innerHTML : '';
    let ventana = window.open('', '', 'width=800,height=600');
    ventana.document.write('<html><head><title>Historial Cl\u00EDnico</title>');
    ventana.document.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">');
    ventana.document.write('<style>@media print { .print-text-black, .text-warning, .text-info, .text-success, .text-danger, .text-primary, .text-secondary, .text-light, .text-white, .text-purple { color: black !important; } .badge { color: black !important; border: 1px solid black !important; background: transparent !important; } body { color: black !important; } }</style>');
    ventana.document.write('</head><body><div class="container mt-4">');
    ventana.document.write('<h2>Historial Cl\u00EDnico del Paciente</h2><hr>');
    ventana.document.write(contenido.replace(/\u00B4C/g, 'C'));
    ventana.document.write('</div></body></html>');
    ventana.document.close();
    setTimeout(() => { ventana.print(); ventana.close(); }, 500);
}'''

if old_func:
    # Handle duplicates if present (the cat output showed it twice?)
    c = c.replace(old_func.group(0), new_func)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
