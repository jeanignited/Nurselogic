import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the broken replacement
bad_str = '<span class="badge bg-secondary me-2 mb-2 px-3 py-2" style="font-size: 0.85rem;"><i class="bi bi-activity text-info me-1"></i> </span>'
good_str = '<span class="badge bg-secondary me-2 mb-2 px-3 py-2" style="font-size: 0.85rem;"><i class="bi bi-activity text-info me-1"></i>$1 $2</span>'

c = c.replace(bad_str, good_str)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("scripts.jsp regex vars fixed.")
