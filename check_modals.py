with open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'imprimirFactura()' in line:
        print(f"Line {i+1}: {line.strip()}")
