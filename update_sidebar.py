import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Make the brand area clickable
old_brand = '''<div class="p-4 d-flex align-items-center mb-2" style="border-bottom: var(--glass-border); flex-shrink: 0;">
            <i class="bi bi-activity text-primary fs-3 me-3" style="filter: drop-shadow(0 0 8px var(--accent));"></i>
            <span class="brand-title fw-bold fs-5 tracking-wide">NURSELOGIC</span>
        </div>'''

new_brand = '''<div class="p-4 d-flex align-items-center mb-2" style="border-bottom: var(--glass-border); flex-shrink: 0; cursor: pointer; transition: 0.3s;" onclick="cambiarVista('dashboard')" onmouseover="this.style.background='rgba(56,189,248,0.1)'" onmouseout="this.style.background='transparent'">
            <i class="bi bi-activity text-primary fs-3 me-3" style="filter: drop-shadow(0 0 8px var(--accent));"></i>
            <span class="brand-title fw-bold fs-5 tracking-wide text-white">NURSELOGIC</span>
        </div>'''

c = c.replace(old_brand, new_brand)

# Remove the inline styles from ul that might conflict, keep overflow-y-auto so ONLY the UL scrolls
c = c.replace('<ul class="nav flex-column flex-nowrap overflow-y-auto" style="display: flex; flex-direction: column; flex-grow: 1; height: 100%;">', '<ul class="nav flex-column flex-nowrap overflow-y-auto" style="display: flex; flex-direction: column; flex-grow: 1; overflow-x: hidden;">')

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated sidebar.jsp brand click')
