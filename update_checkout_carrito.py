import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_checkout = '''            let payload = carritoVentas.map(item => item.id + ":" + item.cantidad).join(",");
            let clienteNombre = document.getElementById("ventaClienteCarrito") ? document.getElementById("ventaClienteCarrito").value.trim() : "Consumidor Final";
            let clienteCedula = document.getElementById("ventaCedulaCarrito") ? document.getElementById("ventaCedulaCarrito").value.trim() : "";
            
            var formData = new URLSearchParams();
            formData.append("action", "facturarCarrito");
            formData.append("payload", payload);
            formData.append("cliente", clienteNombre);
            formData.append("cedula", clienteCedula);
            
            fetch("adminAction", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: formData.toString()
            }).then(() => {
                Swal.fire({title: 'Venta procesada exitosamente!', text: 'Se gener\xf3 la factura correspondiente.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    carritoVentas = [];
                    window.location.href = "dashboard";
                });
            }).catch(e => {
                Swal.fire('Error', 'Hubo un problema al procesar la venta.', 'error');
            });'''

# Let's find the Promise.all logic and replace it with this single fetch
pattern = r'let promises = carritoVentas\.map\(item => \{.*?\}\);\s*Promise\.all\(promises\)\.then\(\(\) => \{.*?\n\s*\}\)\.catch\(e => \{.*?\n\s*\}\);'
c = re.sub(pattern, new_checkout, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated procesarCheckout to use facturarCarrito')
