import io

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('request.getRequestDispatcher("/dashboard").forward(request, response); else {\n            response.sendRedirect("dashboard");\n        }', 'request.getRequestDispatcher("/dashboard").forward(request, response);')

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed syntax error")
