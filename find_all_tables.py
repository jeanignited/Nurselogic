with open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '<table' in line:
        for j in range(max(0, i-4), i+2):
            print(lines[j].strip())
        print("-------")
