with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

open_p = 0
for i in range(3200):
    open_p += lines[i].count('(') - lines[i].count(')')

for i in range(3200, 3300):
    open_p += lines[i].count('(') - lines[i].count(')')
    if i % 10 == 0:
        print(f"Line {i}, open_p: {open_p}")
