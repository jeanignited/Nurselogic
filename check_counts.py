import sys
with open('lint.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Parens:", js.count('('), "-", js.count(')'))
print("Braces:", js.count('{'), "-", js.count('}'))
