import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Card container replacement
c = c.replace('<div class="form-section mt-0 d-flex flex-column h-100 justify-content-between">\\n                        <div>\\n                            <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita', '<div class="form-section mt-0">\\n                        <div>\\n                            <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita')

# 2. Button replacement
c = c.replace('class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>', 'class="btn btn-primary w-100 py-3 fs-5 mb-2"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp updated.")
