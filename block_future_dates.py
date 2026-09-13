import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will replace the input tags in exportarFacturasFechas to have max="' + today + '"
# Let's just find and replace the whole function

old_facturas = '''window.exportarFacturasFechas = function() {
    Swal.fire({
        title: 'Exportar Reporte de Ventas',
        html: '<div class="text-start">' +
              '<label class="form-label small text-secondary">Desde:</label>' +
              '<input type="date" id="expDesde" class="form-control mb-3 bg-transparent text-white border-secondary">' +
              '<label class="form-label small text-secondary">Hasta:</label>' +
              '<input type="date" id="expHasta" class="form-control bg-transparent text-white border-secondary">' +
              '</div>','''

new_facturas = '''window.exportarFacturasFechas = function() {
    let today = new Date().toISOString().split('T')[0];
    Swal.fire({
        title: 'Exportar Reporte de Ventas',
        html: '<div class="text-start">' +
              '<label class="form-label small text-secondary">Desde:</label>' +
              '<input type="date" id="expDesde" class="form-control mb-3 bg-transparent text-white border-secondary" max="' + today + '">' +
              '<label class="form-label small text-secondary">Hasta:</label>' +
              '<input type="date" id="expHasta" class="form-control bg-transparent text-white border-secondary" max="' + today + '">' +
              '</div>','''

c = c.replace(old_facturas, new_facturas)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Blocked future dates in exportarFacturasFechas')
