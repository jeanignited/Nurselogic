import io
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('result = adminService.procesarVentaCarrito(request.getParameter("payload"), request.getParameter("cliente"));', 'result = adminService.procesarVentaCarrito(request.getParameter("payload"), request.getParameter("cliente"), request.getParameter("cedula"));')

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated AdminActionServlet.java')
