import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'<div class="row g-4 mb-5">(\s*<div class="col-md-6">\s*<label class="form-label small text-secondary fw-semibold">Fecha</label>)'
c = re.sub(pattern, r'<div class="row g-4">\1', c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Regex margin adjusted.")
