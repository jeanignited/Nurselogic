import io
import re

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'String fecha = request\.getParameter\("fecha"\);\s*String hora = request\.getParameter\("hora"\);', c)
if m:
    replacement = '''String fecha = request.getParameter("fecha");
        String hora = request.getParameter("hora");
        
        String fechaHora = request.getParameter("fechaHora");
        if (fechaHora != null && !fechaHora.trim().isEmpty() && fechaHora.contains("T")) {
            String[] parts = fechaHora.split("T");
            fecha = parts[0];
            hora = parts[1];
        }'''
    c = c.replace(m.group(0), replacement)
    
    # Fix redirect
    # request.getRequestDispatcher("/dashboard").forward(request, response);
    c = c.replace('request.getRequestDispatcher("/dashboard").forward(request, response);',
                  '''String referer = request.getHeader("Referer");
        if (referer != null && referer.contains("agenda")) {
            response.sendRedirect("agenda");
        } else {
            response.sendRedirect("dashboard");
        }''')
    
    with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed CitaServlet")
