# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_func = '''window.simularAperturaDocumento = function(tipo) {
    alert("Generando " + tipo + " en formato PDF... El documento se abrira en una nueva pestana.");
};'''

# User's exact code with JSP EL escapes (\${)
new_func = '''window.simularAperturaDocumento = function(tipo) {
    let ventana = window.open('', '_blank');
    ventana.document.write(`
        <html>
        <head>
            <title>\${tipo} - NurseLogic</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="p-5">
            <div class="container border p-5 shadow-sm">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h2 class="text-primary mb-0"><strong>NURSELOGIC</strong></h2>
                    <span class="badge bg-secondary">Documento Oficial</span>
                </div>
                <hr>
                <h3 class="mb-4 text-uppercase">\${tipo}</h3>
                <p><strong>Fecha de impresi\u00F3n:</strong> \${new Date().toLocaleDateString()}</p>
                <div class="bg-light p-4 border rounded mt-4">
                    <p class="mb-0">Este es un comprobante digital de su <strong>\${tipo.toLowerCase()}</strong>. En este formato de pre-visualizaci\u00F3n puede guardar el historial m\u00E9dico como archivo PDF para sus registros personales o presentarlo en farmacias afiliadas.</p>
                </div>
                <div class="mt-5 text-center text-muted">
                    <p><small>Generado autom\u00E1ticamente por el Sistema de Salud NurseLogic</small></p>
                </div>
            </div>
            <script>
                window.onload = function() { 
                    setTimeout(function() { window.print(); }, 500);
                }
            </script>
        </body>
        </html>
    `);
    ventana.document.close();
};'''

if old_func in c:
    c = c.replace(old_func, new_func)
    with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated dashboard.jsp")
else:
    print("ERROR: old_func not found!")
