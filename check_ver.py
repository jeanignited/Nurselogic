import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function verFichaClinica\(cedula\).*?\}\)\;', c, re.DOTALL)
if m:
    print(m.group(0))
