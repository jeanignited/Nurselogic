import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace <div class="row g-4 mb-5"> with <div class="row g-4"> to remove the excess margin now that the info box is there.
c = c.replace('<div class="row g-4 mb-5">\\n                                      <div class="col-md-6">\\n                                          <label class="form-label small text-secondary fw-semibold">Fecha</label>', '<div class="row g-4">\\n                                      <div class="col-md-6">\\n                                          <label class="form-label small text-secondary fw-semibold">Fecha</label>')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Margin adjusted.")
