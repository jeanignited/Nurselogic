import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('opacity: 0.6;', 'opacity: 1;')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated canvas opacity')
