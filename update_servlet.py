import io, re

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_actions = '''} else if ("facturarCarrito".equals(action)) {
                  result = adminService.procesarVentaCarrito(request.getParameter("payload"), request.getParameter("cliente"));
              } else if ("ajustarStockMultiple".equals(action)) {
                  result = adminService.ajustarStockMultiple(request.getParameter("payload"));
              } else if ("facturarVenta".equals(action)) {'''

c = c.replace('} else if ("facturarVenta".equals(action)) {', new_actions)

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated AdminActionServlet.java")
