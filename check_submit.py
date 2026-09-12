with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '.submit()' in line:
        print(f"Line {i+1}: {line.strip()}")
