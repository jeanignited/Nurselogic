import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "getElementById('cedulaBusqueda')" in line:
        for j in range(i, min(len(lines), i+30)):
            if "function" in lines[j] or "fetch" in lines[j] or "nombres" in lines[j]:
                print(lines[j].strip())
