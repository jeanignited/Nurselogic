import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'<div>\s*<h6 class="fw-bold text-secondary"><i class="bi bi-capsule me-2"></i>Receta M[^\n]+</h6>\s*<div class="p-3 rounded" [^>]+ id="verDiagReceta"></div>\s*</div>', '', c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
