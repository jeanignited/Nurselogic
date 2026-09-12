import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'dula:')
print(repr(c[idx-5:idx+5]))
