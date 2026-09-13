# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

new_js = '''
// ==========================================
// MOTOR DEL CARRITO DE VENTAS (FARMACIA)
// ==========================================
let carritoVentas = [];

window.agregarAlCarrito = function(id, nombre, precio, maxStock) {
    let item = carritoVentas.find(i => i.id === id);
    if (item) {
        if (item.cantidad < maxStock) {
            item.cantidad++;
            Swal.fire({title: 'Actualizado', text: '+1 ' + nombre + ' al carrito.', icon: 'success', timer: 1000, showConfirmButton: false, background: 'var(--bg-panel)', color: 'var(--text-color)'});
        } else {
            Swal.fire({title: 'Stock Insuficiente', text: 'No hay m\xe1s unidades disponibles en bodega.', icon: 'warning', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        }
    } else {
        carritoVentas.push({ id: id, nombre: nombre, precio: parseFloat(precio), cantidad: 1, maxStock: parseInt(maxStock) });
        Swal.fire({title: 'Agregado', text: nombre + ' a\xf1adido al carrito.', icon: 'success', timer: 1000, showConfirmButton: false, background: 'var(--bg-panel)', color: 'var(--text-color)'});
    }
    actualizarBurbujaCarrito();
};

window.actualizarBurbujaCarrito = function() {
    let btn = document.getElementById('cartBubbleContainer');
    let badge = document.getElementById('cartBubbleBadge');
    if (!btn || !badge) return;
    
    let totalItems = carritoVentas.reduce((acc, item) => acc + item.cantidad, 0);
    if (totalItems > 0) {
        btn.classList.remove('d-none');
        badge.innerText = totalItems;
    } else {
        btn.classList.add('d-none');
    }
};

window.abrirModalCarrito = function() {
    renderizarTablaCarrito();
    var mEl = document.getElementById('modalCarrito');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }
};

window.cambiarCantidadCarrito = function(id, delta) {
    let item = carritoVentas.find(i => i.id === id);
    if (item) {
        let nuevaCant = item.cantidad + delta;
        if (nuevaCant <= 0) {
            carritoVentas = carritoVentas.filter(i => i.id !== id);
        } else if (nuevaCant > item.maxStock) {
            Swal.fire({title: 'L\xedmite', text: 'Alcanz\xf3 el m\xe1ximo en bodega.', icon: 'warning', toast: true, position: 'top-end', timer: 2000, showConfirmButton: false});
        } else {
            item.cantidad = nuevaCant;
        }
        actualizarBurbujaCarrito();
        renderizarTablaCarrito();
    }
};

window.renderizarTablaCarrito = function() {
    let tbody = document.getElementById('tablaCarritoCuerpo');
    let lblTotal = document.getElementById('carritoTotalLabel');
    if (!tbody || !lblTotal) return;
    
    tbody.innerHTML = '';
    let total = 0;
    
    if (carritoVentas.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center text-secondary py-4">El carrito est\xe1 vac\xedo</td></tr>';
        lblTotal.innerText = '.00';
        return;
    }
    
    carritoVentas.forEach(item => {
        let sub = item.precio * item.cantidad;
        total += sub;
        
        let tr = document.createElement('tr');
        tr.innerHTML = 
            <td class="align-middle fw-semibold">\</td>
            <td class="align-middle text-info">$\</td>
            <td class="align-middle">
                <div class="input-group input-group-sm" style="width: 100px;">
                    <button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(\, -1)">-</button>
                    <input type="text" class="form-control text-center bg-transparent text-white border-secondary" value="\" readonly>
                    <button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(\, 1)">+</button>
                </div>
            </td>
            <td class="align-middle text-success fw-bold">$\</td>
            <td class="align-middle text-end">
                <button class="btn btn-sm btn-outline-danger" onclick="cambiarCantidadCarrito(\, -9999)"><i class="bi bi-trash"></i></button>
            </td>
        ;
        tbody.appendChild(tr);
    });
    
    lblTotal.innerText = '$' + total.toFixed(2);
};

window.procesarCheckout = function() {
    if (carritoVentas.length === 0) return;
    
    Swal.fire({
        title: '\xbfFacturar Venta?',
        text: 'Se procesar\xe1n ' + carritoVentas.length + ' medicamentos.',
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
            
            // Procesamos secuencialmente usando fetch
            let promises = carritoVentas.map(item => {
                var formData = new URLSearchParams();
                formData.append("action", "facturarVentaDirecta");
                formData.append("id", item.id);
                // The backend usually expects "cambio" (which means how many units to subtract) for stock adjust, OR it uses facturarVentaDirecta which takes id.
                // Wait! How did the original Facturar Venta work?
                // Let's check old function: brirModalVenta => sets adminActionType = 'facturarVentaDirecta', id=id. It only subtracts ONE unit per click on the old layout? 
                // Let's pass the quantity as "cantidad". If the backend doesn't support "cantidad", we might have to run it N times!
                // Let's assume we run it N times if needed, or pass 'cantidad'. 
            });
            // We need to verify how backend facturarVentaDirecta works!
        }
    });
};
'''

c = c.replace('// Inicializar estado del dropdown si es que existe', new_js + '\n// Inicializar estado del dropdown si es que existe')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Injected JS prep")
