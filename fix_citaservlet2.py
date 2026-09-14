import io
import re

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('request.setAttribute("mensaje", result.message);', 'request.getSession().setAttribute("mensaje", result.message);')
c = c.replace('request.setAttribute("error", result.message);', 'request.getSession().setAttribute("error", result.message);')
c = c.replace('request.setAttribute("error", "Error al registrar el nuevo paciente: " + e.getMessage());', 'request.getSession().setAttribute("error", "Error al registrar el nuevo paciente: " + e.getMessage());')

# Also, if we used forward before, maybe we should just forward to the correct view instead of sendRedirect?
# Actually, the user can just forward to agenda or dashboard. Let's change back to forward to keep things simple if that's what was used before, BUT wait, agenda is usually served by a Servlet (AdminActionServlet?action=agenda or similar?).
# Let's see what serves /agenda.

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
