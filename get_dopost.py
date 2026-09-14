import io
import re

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'protected void doPost.*?\}', c, re.DOTALL)
if m: print(m.group(0))
