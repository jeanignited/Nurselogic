with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Agenda M&eacute;dica y Citas Programadas' in line or 'Agenda' in line and 'Citas' in line:
        print(f'Found at line {i+1}: {line.strip()}')
