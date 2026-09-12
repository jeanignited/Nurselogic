import io
with io.open('lint.js', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('function actualizarGraficos()')
print(c[idx:idx+2500])
