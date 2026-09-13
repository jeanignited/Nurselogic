with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'id="vista-recetas"' in line:
        for j in range(i+20, i+45):
            if j < len(lines):
                print(lines[j].strip())
        break
