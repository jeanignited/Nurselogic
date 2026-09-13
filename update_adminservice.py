import io
with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('public ActionResult procesarVentaCarrito(String payload, String cliente) {', 'public ActionResult procesarVentaCarrito(String payload, String cliente, String cedula) {')
c = c.replace('factura.setClienteNombre(cliente != null && !cliente.trim().isEmpty() ? cliente : "Consumidor Final");', 'factura.setClienteNombre(cliente != null && !cliente.trim().isEmpty() ? cliente : "Consumidor Final");\n            factura.setClienteCedula(cedula);')

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated AdminService.java')
