import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'finalHtml =' in line:
        for j in range(i, i+15):
            print(lines[j].strip())
        break
