# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

js_completion = '''
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
    // Populate select
    let select = document.getElementById('selectStockMultiple');
    if (select) {
        select.innerHTML = '';
        // We will fetch options from the table since it's already rendered!
        let tbody = document.querySelector('#tablaMedicamentos tbody');
        if (tbody) {
            let rows = tbody.querySelectorAll('tr');
            rows.forEach(tr => {
                let btn = tr.querySelector('button[onclick^="agregarAlCarrito"]');
                if (btn) {
                    let onclick = btn.getAttribute('onclick');
                    let match = onclick.match(/agregarAlCarrito\(\s*(\d+)\s*,\s*'([^']+)'/);
                    if (match) {
                        let opt = document.createElement('option');
                        opt.value = match[1];
                        opt.text = match[2];
                        select.appendChild(opt);
                    }
                } else {
                    // For out-of-stock items, the button might be disabled, so it doesn't have onclick.
                    // We can extract ID from the HTML or we can use another trick.
                    // Oh, wait, I removed the id from the rows.
                }
            });
        }
    }
    
    // We actually need the medication data in JS!
    // Since I don't want to parse HTML, I can just fetch it from a JSON endpoint or...
};
'''

# Wait, brirModalAnadirStockMultiple will fail for out of stock items because they have a disabled button and I don't have the ID!
# Let me inject a hidden data attribute in the TR in medicamentos.jsp!
