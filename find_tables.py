with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_pac = False
for i, line in enumerate(lines):
    if '<div id="dashboard_paciente"' in line:
        in_pac = True
    if in_pac and '<table' in line:
        for j in range(max(0, i-5), i+5):
            print(lines[j].strip())
        print("-------")
