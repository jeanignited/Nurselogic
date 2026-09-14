import io
import re

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'// Lista de Citas.*?request\.setAttribute\("listaCitasAdmin", [^)]+\);', c, re.DOTALL)
if m: print(m.group(0))
else:
    m = re.search(r'List<Map<String, String>> listaCitas.*?\} catch', c, re.DOTALL)
    if m: print(m.group(0))
