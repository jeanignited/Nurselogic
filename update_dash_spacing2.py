import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Card container replacement using re.sub
# Search for <div class="col-md-7"> ... <div class="form-section mt-0 d-flex flex-column h-100 justify-content-between"> ... <div> ... <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita
pattern = r'<div class="col-md-7">\s*<div class="form-section mt-0 d-flex flex-column h-100 justify-content-between">\s*<div>\s*<h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita'
replacement = '<div class="col-md-7">\\n                    <div class="form-section mt-0">\\n                        <div>\\n                            <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita'
c = re.sub(pattern, replacement, c)

# 2. Button replacement
c = re.sub(r'class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>', 'class="btn btn-primary w-100 py-3 fs-5 mb-2"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>', c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp regex replaced.")
