import re

with open('lint.js', 'r', encoding='utf-8') as f:
    js = f.read()

def check_syntax(code):
    open_b = 0
    open_p = 0
    in_str = False
    str_c = ''
    in_comment_s = False
    in_comment_m = False
    escape = False
    
    for i, c in enumerate(code):
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
            
        if in_comment_s:
            if c == '\n':
                in_comment_s = False
            continue
            
        if in_comment_m:
            if c == '/' and code[i-1] == '*':
                in_comment_m = False
            continue
            
        if in_str:
            if c == str_c:
                in_str = False
            continue
            
        if c in ('"', "'", ''):
            in_str = True
            str_c = c
            continue
            
        if c == '/' and i+1 < len(code) and code[i+1] == '/':
            in_comment_s = True
            continue
            
        if c == '/' and i+1 < len(code) and code[i+1] == '*':
            in_comment_m = True
            continue
            
        if c == '{': open_b += 1
        elif c == '}': open_b -= 1
        elif c == '(': open_p += 1
        elif c == ')': open_p -= 1
        
        if open_b < 0:
            print("Negative brace at index", i)
            return
        if open_p < 0:
            print("Negative paren at index", i)
            return
            
    print(f"Final braces: {open_b}, Parens: {open_p}")

check_syntax(js)
