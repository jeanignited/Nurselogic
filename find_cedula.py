import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I need to wrap document.getElementById('cedulaBusqueda').addEventListener('keyup', function() {
# Wait, let's find that block and replace it.
pattern = r"document\.getElementById\('cedulaBusqueda'\)\.addEventListener\('keyup',\s*function\(\)\s*{"

# Check what the block looks like
idx = c.find("document.getElementById('cedulaBusqueda').addEventListener('keyup', function() {")
if idx != -1:
    print("Found it!")
    print(c[idx:idx+200])
else:
    print("Not found exactly.")
