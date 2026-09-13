import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the Agendar Cita form-section
c = c.replace('<div class="form-section mt-0">\\n                          <div>\\n                              <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita', '<div class="form-section mt-0 h-100 d-flex flex-column">\\n                          <div class="d-flex flex-column flex-grow-1">\\n                              <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita')

# Make the form flex column flex-grow-1 so mt-auto works inside it
c = c.replace('<form action="agendarCita" method="post" autocomplete="off">', '<form action="agendarCita" method="post" autocomplete="off" class="d-flex flex-column flex-grow-1">')

# Add mt-auto to the button and remove mb-2
c = c.replace('<button type="submit" class="btn btn-primary w-100 py-3 fs-5 mb-2"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>', '<button type="submit" class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>')


with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updates applied.")
