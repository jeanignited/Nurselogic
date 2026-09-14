import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'abrirModalVerDiagnostico' in line or 'abrirModalVerDiagnosticoCama' in line or 'imprimirHistorialMedico' in line:
        print(f"Line {i+1}: {line.strip()}")
