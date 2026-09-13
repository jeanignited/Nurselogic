import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# I will wrap the doget block with try-catch and print the error
old_doget = '''    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String tipo = request.getParameter("tipo");'''

new_doget = '''    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        try {
            String tipo = request.getParameter("tipo");'''

c = c.replace(old_doget, new_doget)
c = c.replace('} else {\n            response.sendRedirect("dashboard");\n        }\n    }', '} else {\n            response.sendRedirect("dashboard");\n        }\n        } catch(Exception e) {\n            response.setContentType("text/plain");\n            e.printStackTrace(response.getWriter());\n        }\n    }')

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Patched ExportServlet to print stack trace')
