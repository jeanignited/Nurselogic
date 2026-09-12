import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()

c = c.replace(b'\xbf', b'\xc2\xbf')
c = c.replace(b'\xed', b'\xc3\xad') # í
c = c.replace(b'\xf3', b'\xc3\xb3') # ó

with io.open('src/main/webapp/includes/scripts.jsp', 'wb') as f:
    f.write(c)

print("Fixed swal encoding")
