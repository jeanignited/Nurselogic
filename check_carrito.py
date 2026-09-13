import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="modalCarrito"')
idx2 = text.find('</table', idx)
print(text[idx:idx2+10])
