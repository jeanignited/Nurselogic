import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "Ficha M\u00E9dica Integral" in line or "Ficha M\ufffddica Integral" in line or "Ficha M" in line:
        if "Integral" in line:
            for j in range(i, min(len(lines), i+40)):
                print(lines[j].rstrip())
            break
