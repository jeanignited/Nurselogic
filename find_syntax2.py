with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()
stack = []
for i, char in enumerate(c):
    if char == '(': stack.append((char, i))
    elif char == ')': 
        if stack: stack.pop()
        else: print('Extra ) at', i)
print('Remaining unclosed:', stack)
