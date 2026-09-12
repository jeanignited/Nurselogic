import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('function cambiarEstadoCita')
idx2 = c.find('}', c.find('f.submit();', idx)) + 1
print(c[idx:idx2+100])
