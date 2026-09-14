import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'function imprimirHistorialMedico(' in line:
        skip = True
    if skip and '</script>' in line:
        skip = False
    
    if not skip:
        new_lines.append(line)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write("".join(new_lines))
