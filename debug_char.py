import io
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('dula')
print(repr(c[idx-2:idx+4]))
