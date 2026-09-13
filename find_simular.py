with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'window.simularAperturaDocumento' in line:
        for j in range(max(0, i-2), min(len(lines), i+8)):
            print(lines[j].strip())
        break
