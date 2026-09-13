import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

js_func = '''
window.exportarFacturasFechas = function() {
    Swal.fire({
        title: 'Exportar Reporte de Ventas',
        html: '<div class="text-start">' +
              '<label class="form-label small text-secondary">Desde:</label>' +
              '<input type="date" id="expDesde" class="form-control mb-3 bg-transparent text-white border-secondary">' +
              '<label class="form-label small text-secondary">Hasta:</label>' +
              '<input type="date" id="expHasta" class="form-control bg-transparent text-white border-secondary">' +
              '</div>',
        background: 'var(--bg-panel)', color: 'var(--text-color)',
        showCancelButton: true, confirmButtonText: 'Exportar', cancelButtonText: 'Cancelar'
    }).then(res => {
        if (res.isConfirmed) {
            let d = document.getElementById('expDesde').value;
            let h = document.getElementById('expHasta').value;
            window.location.href = "exportCsv?tipo=facturas&desde=" + d + "&hasta=" + h;
        }
    });
};
'''
if 'exportarFacturasFechas' not in c:
    c = c + js_func
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
print('Added exportarFacturasFechas to scripts.jsp')
