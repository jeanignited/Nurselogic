import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()
idx = c.find(b'M\xc3\xa9dico')
if idx != -1: print('Found M\xc3\xa9dico')
else: print('Not found')
idx = c.find(b'M\xc3\x83\xc2\xa9dico')
if idx != -1: print('Found double encoded')
