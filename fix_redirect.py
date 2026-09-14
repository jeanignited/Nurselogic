import io
import re

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'String referer = request\.getHeader\("Referer"\);.*?\}', c, re.DOTALL)
if m:
    c = c.replace(m.group(0), 'request.getRequestDispatcher("/dashboard").forward(request, response);')
    with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Reverted redirect")
else:
    print("Not found")
