import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_func = False
for i, line in enumerate(lines):
    if 'function calcularEdadTiempoReal' in line:
        in_func = True
    if in_func:
        print(line.rstrip())
        if line.strip() == '}':
            break
