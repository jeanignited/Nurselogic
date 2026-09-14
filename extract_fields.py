import io
import re
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<label class="form-label small text-secondary fw-semibold">Enfermedades Preexistentes.*?<h6 class="text-theme pb-2 mb-4" style="border-bottom: 1px solid rgba\(255,255,255,0\.1\);"><i class="bi bi-heart-pulse text-danger me-2"></i>Signos Vitales</h6>', c, re.DOTALL)
if m:
    with open('admision_fields.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Extracted fields to admision_fields.txt")
