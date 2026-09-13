import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('modalCatalogos')
idx_end = text.find('</form>', idx)
print(text[idx_end-200:idx_end+50])
