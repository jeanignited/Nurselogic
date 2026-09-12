import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()
idx = c.find(b'\xc3\x83')
if idx != -1:
    print(c[idx:idx+25])
else:
    print("Not found")
