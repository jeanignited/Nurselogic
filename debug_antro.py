import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'Antropom')
print(repr(c[idx-10:idx+30]))
