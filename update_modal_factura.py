import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cerrar</button>', '<button type="button" class="btn btn-outline-info px-4 me-auto" onclick="window.print()"><i class="bi bi-printer"></i> Imprimir</button>\n          <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cerrar</button>')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated modalDetalleFactura with Imprimir button')
