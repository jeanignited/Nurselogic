import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_cb = False
for i, line in enumerate(lines):
    if "let cb = document.getElementById('cedulaBusqueda');" in line:
        in_cb = True
    if in_cb:
        if "document.addEventListener('DOMContentLoaded'" in line:
            break
        print(line.rstrip())
