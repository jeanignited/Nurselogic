with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'id="vista-citas"' in line:
        for j in range(i, i+30):
            if j < len(lines):
                print(lines[j].strip())
        break
