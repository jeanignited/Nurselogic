import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('catAlergiaCampos')
print(text[idx-50:idx+400])
