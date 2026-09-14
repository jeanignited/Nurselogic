import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_f = False
for line in lines:
    if 'function calcularEdadTiempoReal' in line:
        in_f = True
    if in_f:
        print(line.rstrip())
        if 'document.getElementById(' in line and 'nombres' in line:
            pass
