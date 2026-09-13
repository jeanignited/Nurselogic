import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Just use regex to strip out the style block and replace the select element
c = re.sub(r'<style>\s*\.scrollable-select:focus.*?height: auto;\s*\}\s*</style>', '', c, flags=re.DOTALL)
c = re.sub(r'<select name="especialidad".*?onchange="this\.size=1; this\.blur\(\);">', '<select name="especialidad" class="form-select form-select-lg shadow-none" required style="border-radius: 10px;">', c, flags=re.DOTALL)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Removed custom select styles properly')
