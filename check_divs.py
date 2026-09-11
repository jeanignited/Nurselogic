import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

div_count = c.count('<div')
end_div_count = c.count('</div')
print(f'<div count: {div_count}')
print(f'</div count: {end_div_count}')
