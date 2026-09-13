import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace <div class="form-section mt-0"> that is right above Agendar Cita
pattern = r'<div class="form-section mt-0">\s*<div>\s*<h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita'
replacement = '<div class="form-section mt-0 h-100 d-flex flex-column">\\n                          <div class="d-flex flex-column flex-grow-1">\\n                              <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita'
c = re.sub(pattern, replacement, c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Regex applied.")
