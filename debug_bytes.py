import io
with io.open('src/main/webapp/views/dashboard.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'dula')
print(repr(c[idx-2:idx+4]))
