import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_footer = '''      <div class="modal-footer border-0">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Seguir Comprando</button>
        <button type="button" class="btn btn-success" onclick="procesarCheckout()"><i class="bi bi-receipt me-2"></i>Facturar Venta</button>
      </div>'''

new_footer = '''      <div class="modal-footer border-0 justify-content-between">
        <button type="button" class="btn btn-outline-danger" onclick="vaciarCarrito()"><i class="bi bi-trash me-2"></i>Vaciar Carrito</button>
        <div>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Seguir Comprando</button>
            <button type="button" class="btn btn-success" onclick="procesarCheckout()"><i class="bi bi-receipt me-2"></i>Facturar Venta</button>
        </div>
      </div>'''

if old_footer in c:
    c = c.replace(old_footer, new_footer)
    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added Vaciar Carrito button")
else:
    print("Could not find footer")
