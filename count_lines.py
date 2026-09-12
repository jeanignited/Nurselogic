with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(3260, 3275):
    line = lines[i]
    print(f"{i}: {line.count('(')} - {line.count(')')} : {line.strip()}")
