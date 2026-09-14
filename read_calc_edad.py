import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function calcularEdadTiempoReal' in line:
        for j in range(i, min(len(lines), i+30)):
            print(lines[j].strip())
        break
