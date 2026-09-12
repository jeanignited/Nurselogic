import io
with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

idx = c.find('card-body')
print(c[idx:idx+1500])
