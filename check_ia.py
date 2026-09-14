import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Inteligencia Cl' in line or 'alertasIA' in line:
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j].strip()}")
        break
