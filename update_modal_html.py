import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<div class="mb-4">\s*<h6 class="fw-bold text-secondary"><i class="bi bi-journal-medical me-2"></i>Diagn\u00F3stico</h6>\s*<div class="p-3 rounded" style="background: rgba\(0,0,0,0\.2\); border: 1px solid rgba\(255,255,255,0\.1\); white-space: pre-wrap;" id="verDiagTexto"></div>\s*</div>', c)
if m:
    c = c.replace(m.group(0), '<div class="mb-4" id="verDiagTexto"></div>')
    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated modals.jsp")
else:
    print("Not found")
