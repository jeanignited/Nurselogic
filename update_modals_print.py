import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="modalVerDiagnostico"' in line:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if 'onclick="imprimirFactura()"' in lines[i]:
        lines[i] = lines[i].replace('onclick="imprimirFactura()"', 'onclick="imprimirHistorialMedico()"')
        print("Replaced at line", i)
        break

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.writelines(lines)
