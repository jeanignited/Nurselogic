import io
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    s = f.read()
s = s.replace('} else if ("crearMedicamento".equals(action)) {', '} else if ("eliminarFactura".equals(action)) {\n                result = adminService.eliminarFactura(request.getParameter("id"));\n            } else if ("crearMedicamento".equals(action)) {')
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
    f.write(s)

print("Added eliminarFactura to servlet")
