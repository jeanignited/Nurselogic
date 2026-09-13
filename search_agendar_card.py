with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Agendar Cita' in line and 'card' in lines[i-5]:
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(lines[j].strip())
        print("----")
