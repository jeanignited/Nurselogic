import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'Cdula')
print(repr(c[max(0,idx-20):idx+20]))

idx2 = c.find(b'ltima')
print(repr(c[max(0,idx2-20):idx2+20]))
