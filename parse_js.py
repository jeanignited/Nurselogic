import sys
with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

in_string = False
string_char = ''
escape = False
stack = []
for i, char in enumerate(c):
    if not in_string:
        if char in ['\"', '\'', '']:
            in_string = True
            string_char = char
        elif char == '(': stack.append((char, i))
        elif char == '{': stack.append((char, i))
        elif char == '[': stack.append((char, i))
        elif char == ')':
            if stack and stack[-1][0] == '(': stack.pop()
            else: print('Extra ) at', i)
        elif char == '}':
            if stack and stack[-1][0] == '{': stack.pop()
            else: print('Extra } at', i)
        elif char == ']':
            if stack and stack[-1][0] == '[': stack.pop()
            else: print('Extra ] at', i)
    else:
        if escape:
            escape = False
        elif char == '\\':
            escape = True
        elif char == string_char:
            in_string = False

print('Remaining unclosed:', stack)
