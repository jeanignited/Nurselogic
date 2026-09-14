import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.search(r'function calcularEdadTiempoReal\(\).*?\}\n', c, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Not found")
