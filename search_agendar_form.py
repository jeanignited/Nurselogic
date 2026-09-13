with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Agendar Cita M&eacute;dica' in line:
        for j in range(max(0, i-5), min(len(lines), i+5)):
            print(lines[j].strip())
        print("----")
