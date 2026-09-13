import io
import re
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_med = text.find('crearMedicamento')
print(text[idx_med-100:idx_med+600])

idx_cat = text.find('crearEnfermedad')
print(text[idx_cat-100:idx_cat+600])

