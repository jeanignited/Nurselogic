import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace procesarCheckout
old_func = '''window.procesarCheckout = function() {
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
                // Let's check old function:  brirModalVenta => sets adminActionType = 'facturarVentaDirecta', id=id. It only subtracts ONE unit per click on the old layout? 
                // Let's pass the quantity as "cantidad". If the backend doesn't support "cantidad", we might have to run it N times!
                // Let's assume we run it N times if needed, or pass 'cantidad'. 
            });
            // We need to verify how backend facturarVentaDirecta works!
        }
    });
};'''

new_func = '''window.procesarCheckout = function() {
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
            
            let promises = carritoVentas.map(item => {
                var formData = new URLSearchParams();
                formData.append("action", "facturarVenta");
                formData.append("idMed", item.id);
                formData.append("cantidad", item.cantidad);
                formData.append("cliente", "Consumidor Final (Carrito)");
                
                return fetch("adminAction", {
                    method: "POST",
                    headers: { "Content-Type": "application/x-www-form-urlencoded" },
                    body: formData.toString()
                });
            });
            
            Promise.all(promises).then(() => {
                Swal.fire({title: 'Venta procesada exitosamente!', text: 'Se generaron las facturas correspondientes.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    carritoVentas = [];
                    window.location.href = "dashboard";
                });
            }).catch(e => {
                Swal.fire('Error', 'Hubo un problema al procesar la venta.', 'error');
            });
        }
    });
};'''

# Need to be careful with the exact original text since it might have non-ASCII \xe1 characters and exact indentation
# So let's use regex to find the function block
c = re.sub(r'window\.procesarCheckout = function\(\) \{.*?\n\};', new_func, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated procesarCheckout')
