import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

c = c.replace(b'Cdula:', b'C\xc3\xa9dula:')

with io.open('src/main/webapp/includes/modals.jsp', 'wb') as f:
    f.write(c)

print("Fixed Cdula:")
