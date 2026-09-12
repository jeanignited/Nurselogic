with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'chartEspInst' in line:
        print(i, line.strip())
