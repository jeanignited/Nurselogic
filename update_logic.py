# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# I will replace window.procesarCheckout = function() { ... }; with the full implementation
old_checkout = r'window\.procesarCheckout = function\(\) \{.*?\}\s*\n\s*\/\/ We need to verify how backend facturarVentaDirecta works!\s*\n\s*\}\s*\}\);\s*\};'

new_checkout = '''
window.procesarCheckout = function() {
    if (carritoVentas.length === 0) return;
    
    Swal.fire({
        title: 'Facturar Venta',
        html: '<div class="mb-3 text-start"><label class="form-label text-secondary small">Nombre del Cliente (Opcional)</label><input type="text" id="carritoCliente" class="form-control" placeholder="Consumidor Final" style="background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); color: white;"></div>',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#10b981',
        confirmButtonText: 'S\xed, Facturar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({title: 'Procesando...', text: 'Registrando ventas...', allowOutsideClick: false, background: 'var(--bg-panel)', color: 'var(--text-color)', didOpen: () => { Swal.showLoading(); }});
            
            let cliente = document.getElementById('carritoCliente') ? document.getElementById('carritoCliente').value.trim() : '';
            let payload = carritoVentas.map(item => item.id + ':' + item.cantidad).join(',');
            
            var formData = new URLSearchParams();
            formData.append("action", "facturarCarrito");
            formData.append("payload", payload);
            formData.append("cliente", cliente);

            fetch('adminAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Venta Completada', text: 'Se ha generado la factura correctamente.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard?vista=facturas";
                });
            });
        }
    });
};

window.abrirModalAnadirStockMultiple = function() {
    let select = document.getElementById('selectStockMultiple');
    let container = document.getElementById('camposStockDinamicos');
    if (!select || !container) return;
    
    select.innerHTML = '';
    container.innerHTML = '';
    
    let tbody = document.querySelector('#tablaMedicamentos tbody');
    if (tbody) {
        let rows = tbody.querySelectorAll('tr[data-id]');
        rows.forEach(tr => {
            let id = tr.getAttribute('data-id');
            let nombre = tr.getAttribute('data-nombre');
            let opt = document.createElement('option');
            opt.value = id;
            opt.text = nombre;
            select.appendChild(opt);
        });
    }
    
    var mEl = document.getElementById('modalAnadirStockMultiple');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }
};

window.renderizarCamposStock = function() {
    let select = document.getElementById('selectStockMultiple');
    let container = document.getElementById('camposStockDinamicos');
    if (!select || !container) return;
    
    let selectedOptions = Array.from(select.selectedOptions);
    
    // Solo mantener los inputs de las opciones seleccionadas, agregar los nuevos
    let currentInputs = Array.from(container.querySelectorAll('.stock-item-input'));
    let currentIds = currentInputs.map(el => el.getAttribute('data-med-id'));
    let selectedIds = selectedOptions.map(opt => opt.value);
    
    // Eliminar los no seleccionados
    currentInputs.forEach(el => {
        if (!selectedIds.includes(el.getAttribute('data-med-id'))) {
            el.remove();
        }
    });
    
    // Agregar los nuevos
    selectedOptions.forEach(opt => {
        if (!currentIds.includes(opt.value)) {
            let div = document.createElement('div');
            div.className = 'col-md-6 stock-item-input';
            div.setAttribute('data-med-id', opt.value);
            div.innerHTML = 
                <div class="input-group input-group-sm">
                    <span class="input-group-text bg-dark border-secondary text-white w-50 text-truncate" title="\">\</span>
                    <input type="number" class="form-control text-center stock-qty-input" placeholder="Cant." min="1" value="10">
                </div>
            ;
            container.appendChild(div);
        }
    });
};

window.procesarAbastecimiento = function() {
    let container = document.getElementById('camposStockDinamicos');
    if (!container) return;
    
    let items = Array.from(container.querySelectorAll('.stock-item-input'));
    if (items.length === 0) {
        Swal.fire({text: 'Seleccione al menos un f\xe1rmaco e ingrese las cantidades.', icon: 'warning', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        return;
    }
    
    let payloadArr = [];
    items.forEach(el => {
        let id = el.getAttribute('data-med-id');
        let qty = el.querySelector('input').value;
        if (qty && parseInt(qty) > 0) {
            payloadArr.push(id + ':' + qty);
        }
    });
    
    if (payloadArr.length === 0) return;
    
    Swal.fire({title: 'Procesando...', text: 'Registrando ingresos...', allowOutsideClick: false, background: 'var(--bg-panel)', color: 'var(--text-color)', didOpen: () => { Swal.showLoading(); }});
    
    var formData = new URLSearchParams();
    formData.append("action", "ajustarStockMultiple");
    formData.append("payload", payloadArr.join(','));

    fetch('adminAction', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData.toString()
    }).then(function(response) {
        Swal.fire({title: '\xa1Abastecido!', text: 'El stock de ' + payloadArr.length + ' medicamento(s) ha sido actualizado.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
            window.location.href = "dashboard?vista=medicamentos";
        });
    });
};
'''

c = re.sub(old_checkout, new_checkout, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated JS logic!")
