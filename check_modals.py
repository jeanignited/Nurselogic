import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_enf = text.find('crearEnfermedad')
print(text[idx_enf-200:idx_enf+500])
