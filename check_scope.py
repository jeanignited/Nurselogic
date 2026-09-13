import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('abrirModalCatalogos')
print(text[max(0, idx-200):idx+50])
