# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

new_modals = '''
<!-- Burbuja Flotante Carrito -->
<div id="cartBubbleContainer" class="position-fixed bottom-0 end-0 p-4 d-none" style="z-index: 1050;">
    <button type="button" class="btn btn-info rounded-circle shadow-lg p-3 position-relative" style="width: 60px; height: 60px;" onclick="abrirModalCarrito()">
        <i class="bi bi-cart3 fs-4 text-dark"></i>
        <span id="cartBubbleBadge" class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger shadow-sm" style="font-size: 0.85rem;">
            0
        </span>
    </button>
</div>

<!-- Modal Carrito de Ventas -->
<div class="modal fade" id="modalCarrito" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-cart-check me-2 text-info"></i>Carrito de Facturaci\xf3n</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body pb-0">
        <div class="table-responsive">
            <table class="table table-dark-custom table-sm">
                <thead>
                    <tr>
                        <th>F\xe1rmaco</th>
                        <th>Precio U.</th>
                        <th style="width: 120px;">Cantidad</th>
                        <th>Subtotal</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="tablaCarritoCuerpo">
                    <!-- Dinamico -->
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3" class="text-end fw-bold">TOTAL:</td>
                        <td colspan="2" class="text-success fw-bold fs-5" id="carritoTotalLabel">.00</td>
                    </tr>
                </tfoot>
            </table>
        </div>
      </div>
      <div class="modal-footer border-0 pt-0 mt-2">
        <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Seguir Comprando</button>
        <button type="button" class="btn btn-success px-4 fw-bold shadow-sm text-dark" onclick="procesarCheckout()"><i class="bi bi-receipt me-2"></i>Facturar Venta</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal A\xf1adir Stock M\xfaltiple -->
<div class="modal fade" id="modalAnadirStockMultiple" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); border: var(--glass-border);">
      <div class="modal-header border-0">
        <h5 class="modal-title fw-bold"><i class="bi bi-box-seam me-2" style="color:#a3e635;"></i>Abastecimiento de Bodega</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body pb-0">
        <div class="alert alert-info py-2 small bg-opacity-10 border-0"><i class="bi bi-info-circle me-1"></i> Selecciona uno o varios f\xe1rmacos y asigna cu\xe1ntas unidades nuevas ingresan a bodega.</div>
        <div class="mb-3">
            <label class="form-label small text-secondary">F\xe1rmacos a abastecer</label>
            <select id="selectStockMultiple" class="form-select" multiple size="6" onchange="renderizarCamposStock()">
                <!-- Opciones se llenan por JS -->
            </select>
            <div class="form-text text-secondary">Mant\xe9n presionado Ctrl (o Cmd) para seleccionar m\xfaltiples.</div>
        </div>
        <div id="camposStockDinamicos" class="row g-2 mb-3">
            <!-- Campos din\xe1micos -->
        </div>
      </div>
      <div class="modal-footer border-0 pt-0 mt-3">
        <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Cancelar</button>
        <button type="button" class="btn px-4 fw-bold shadow-sm text-dark" style="background: linear-gradient(135deg, #a3e635, #84cc16);" onclick="procesarAbastecimiento()"><i class="bi bi-check-lg me-1"></i>Registrar Ingreso</button>
      </div>
    </div>
  </div>
</div>
'''

c = c.replace('<!-- Modal Facturar Venta -->', new_modals + '\n<!-- Modal Facturar Venta -->')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated modals.jsp")
