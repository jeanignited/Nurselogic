import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'Dar de Alta')
print(repr(c[idx:idx+150]))
