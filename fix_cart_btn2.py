import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_f = '''      <div class="modal-footer border-0 pt-0 mt-2">
        <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Seguir Comprando</button>
        <button type="button" class="btn btn-success px-4 fw-bold shadow-sm text-dark" onclick="procesarCheckout()"><i class="bi bi-receipt me-2"></i>Facturar Venta</button>
      </div>'''

new_f = '''      <div class="modal-footer border-0 pt-0 mt-2 d-flex justify-content-between w-100">
        <button type="button" class="btn btn-outline-danger px-3" onclick="vaciarCarrito()"><i class="bi bi-trash"></i> Cancelar</button>
        <div>
            <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Seguir</button>
            <button type="button" class="btn btn-success px-4 fw-bold shadow-sm text-dark" onclick="procesarCheckout()"><i class="bi bi-receipt me-1"></i>Facturar</button>
        </div>
      </div>'''

c = c.replace(old_f, new_f)
with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Added Cancel button")
