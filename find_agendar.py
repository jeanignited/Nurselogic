with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Agendar Cita' in line or 'Agendar Nueva Cita' in line:
        for j in range(i-5, i+15):
            if j < len(lines):
                print(lines[j].strip())
        break
