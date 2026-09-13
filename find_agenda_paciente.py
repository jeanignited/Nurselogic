with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_pac = False
for i, line in enumerate(lines):
    if '<div id="dashboard_paciente"' in line:
        in_pac = True
    if in_pac and ('Agenda' in line or 'Cita' in line or 'Programada' in line):
        print(f"Line {i+1}: {line.strip()}")
