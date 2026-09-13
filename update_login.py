import io
import re

with io.open('src/main/java/com/nurselogic/controller/LoginServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('session.setAttribute("nombres", u.getNombres() + " " + u.getApellidos());', 'session.setAttribute("nombres", u.getNombres());\nsession.setAttribute("apellidos", u.getApellidos());')

with io.open('src/main/java/com/nurselogic/controller/LoginServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated LoginServlet.java')
