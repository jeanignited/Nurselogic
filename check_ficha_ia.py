import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Hipertensi' in line or 'alert-warning' in line or 'shock' in line:
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j].strip()}")
        break
