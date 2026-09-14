import io

with io.open('src/main/webapp/views/agendarCita.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Nota importante:' in line:
        for j in range(max(0, i-5), min(len(lines), i+5)):
            print(f"{j+1}: {lines[j].strip()}")
        break
