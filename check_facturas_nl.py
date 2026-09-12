with open('src/main/webapp/views/facturas.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'out.print("<td class=\'pe-4' in line:
        print(f"Line {i+1}: {repr(line)}")
        print(f"Line {i+2}: {repr(lines[i+1])}")
