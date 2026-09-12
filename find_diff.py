with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

open_p = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '(':
            open_p += 1
        elif c == ')':
            open_p -= 1
    
    # Just to get a rough idea where it goes off
    if i % 100 == 0:
        print(f"Line {i}, open_p: {open_p}")
print(f"Final open_p: {open_p}")
