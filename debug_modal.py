import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'modalA')
print(c[idx:idx+30])
