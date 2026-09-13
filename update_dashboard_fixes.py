import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add registration date to Mis Datos Clinicos
old_header = '<h3 class="mb-0 fw-bold" style="color: #10b981;">Mis Datos Cl&iacute;nicos</h3>'
new_header = '''<h3 class="mb-0 fw-bold" style="color: #10b981;">Mis Datos Cl&iacute;nicos</h3>
                    <span class="badge ms-auto py-2 px-3 fw-normal" style="background: rgba(16,185,129,0.1); color: #10b981; border: 1px solid rgba(16,185,129,0.2);">
                        <i class="bi bi-clock-history me-1"></i>Actualizado: <%= java.time.LocalDate.now().toString() %>
                    </span>'''
c = c.replace(old_header, new_header)

# Fix scroll on the select element. By default <select> scroll depends on the OS. 
# We can force a custom visual by adding a size attribute on focus, and removing it on blur/change.
old_select = '<select name="especialidad" class="form-select form-select-lg shadow-none" required style="border-radius: 10px;">'
new_select = '''<style>
                                    .scrollable-select:focus {
                                        position: absolute;
                                        z-index: 10;
                                        height: auto;
                                    }
                                </style>
                                <select name="especialidad" class="form-select form-select-lg shadow-none scrollable-select" required style="border-radius: 10px;" onfocus="this.size=5;" onblur="this.size=1;" onchange="this.size=1; this.blur();">'''
c = c.replace(old_select, new_select)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated dashboard.jsp with date and select fixes')
