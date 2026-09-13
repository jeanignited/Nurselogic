import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('abrirModalEditarEnfermedad')
print(text[idx-50:idx+600])
