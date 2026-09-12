import io, re

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Add to doPost
c = c.replace('} else if ("crear".equals(action)) {', '} else if ("eliminarFactura".equals(action)) {\n                result = adminService.eliminarFactura(id);\n            } else if ("crear".equals(action)) {')

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added to AdminActionServlet")
