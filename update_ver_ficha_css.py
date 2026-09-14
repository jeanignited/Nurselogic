import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function verFichaClinica\(cedula\).*?\}\)\;', c, re.DOTALL)
if m:
    c = c.replace('class="fw-bold text-warning"', 'class="fw-bold text-warning print-text-black"')
    c = c.replace('class="fw-bold text-info"', 'class="fw-bold text-info print-text-black"')
    c = c.replace('class="fw-bold text-success"', 'class="fw-bold text-success print-text-black"')
    c = c.replace('text-warning me-2', 'text-warning print-text-black me-2')
    c = c.replace('text-info me-2', 'text-info print-text-black me-2')
    c = c.replace('text-success me-2', 'text-success print-text-black me-2')
    c = c.replace('text-danger me-2', 'text-danger print-text-black me-2')
    c = c.replace('text-primary me-2', 'text-primary print-text-black me-2')
    
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added print-text-black to scripts.jsp elements")
