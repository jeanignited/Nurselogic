import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'Evaluaci')
print(repr(c[idx:idx+20]))
