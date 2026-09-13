with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_paciente = False
for i, line in enumerate(lines):
    if '<div id="dashboard_paciente"' in line:
        in_paciente = True
    if in_paciente and 'Agenda' in line:
        print(f"Line {i+1}: {line.strip()}")
