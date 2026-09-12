import io, re

with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the action cell
old_td = '''<td class='pe-4 text-center'><button type='button' class='btn btn-sm btn-outline-info rounded-pill px-3' title='Ver Factura' onclick=\\"abrirModalVerFactura('FAC-" + String.format("%05d", f.getId()) + "', '" + f.getClienteNombre().replace("'", "\\\\'") + "', '" + f.getFechaEmision().toString().replace("T", " ").substring(0, 16) + "', '" + String.format("%.2f", f.getTotal()) + "', this)\\" data-detalles=\\"" + detalles.toString().replace("\\"", "&quot;") + "\\"><i class='bi bi-eye me-1'></i> Ver</button></td>'''

new_td = '''<td class='pe-4 text-center'>
    <div class='d-flex justify-content-center gap-2'>
        <button type='button' class='btn btn-sm btn-outline-info rounded-pill px-3' title='Ver Factura' onclick=\\"abrirModalVerFactura('FAC-" + String.format("%05d", f.getId()) + "', '" + f.getClienteNombre().replace("'", "\\\\'") + "', '" + f.getFechaEmision().toString().replace("T", " ").substring(0, 16) + "', '" + String.format("%.2f", f.getTotal()) + "', this)\\" data-detalles=\\"" + detalles.toString().replace("\\"", "&quot;") + "\\"><i class='bi bi-eye me-1'></i> Ver</button>
        " + (isAdmin ? "<form action='facturaAction' method='POST' style='display:inline;' onsubmit='return confirm(\\"¿Eliminar esta factura?\\");'><input type='hidden' name='action' value='eliminar'><input type='hidden' name='id' value='" + f.getId() + "'><button type='submit' class='btn btn-sm btn-outline-danger rounded-pill' title='Eliminar'><i class='bi bi-trash'></i></button></form>" : "") + "
    </div>
</td>'''

c = c.replace(old_td, new_td)

with io.open('src/main/webapp/views/facturas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
