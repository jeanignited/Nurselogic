import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('window.renderizarTablaCarrito = function() {')
idx2 = c.find('window.procesarCheckout = function() {')

if idx1 != -1 and idx2 != -1:
    old_code = c[idx1:idx2]
    new_code = """window.renderizarTablaCarrito = function() {
    let tbody = document.getElementById('tbodyCarrito');
    let totalSpan = document.getElementById('carritoTotal');
    if (!tbody || !totalSpan) return;
    
    tbody.innerHTML = '';
    let total = 0;
    
    if (carritoVentas.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center text-secondary py-4">El carrito est\u00E1 vac\u00EDo</td></tr>';
        totalSpan.innerText = '0.00';
        return;
    }
    
    carritoVentas.forEach(item => {
        let subt = item.precio * item.cantidad;
        total += subt;
        
        let tr = document.createElement('tr');
        tr.innerHTML = 
            '<td class="align-middle fw-semibold">' + item.nombre + '</td>' +
            '<td class="align-middle text-info">$' + item.precio.toFixed(2) + '</td>' +
            '<td class="align-middle">' +
                '<div class="input-group input-group-sm" style="width: 100px;">' +
                    '<button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(' + item.id + ', -1)">-</button>' +
                    '<input type="text" class="form-control text-center bg-transparent text-white border-secondary" value="' + item.cantidad + '" readonly>' +
                    '<button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(' + item.id + ', 1)">+</button>' +
                '</div>' +
            '</td>' +
            '<td class="align-middle text-success fw-bold">$' + subt.toFixed(2) + '</td>' +
            '<td class="align-middle text-end">' +
                '<button class="btn btn-sm btn-outline-danger" onclick="cambiarCantidadCarrito(' + item.id + ', -9999)"><i class="bi bi-trash"></i></button>' +
            '</td>';
        tbody.appendChild(tr);
    });
    
    totalSpan.innerText = total.toFixed(2);
};

"""
    c = c.replace(old_code, new_code)
    
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed renderizarTablaCarrito!")
else:
    print("Could not find boundaries")
