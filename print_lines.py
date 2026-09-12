with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(3260, 3275):
    print(f"{i}: {lines[i].strip()}")
