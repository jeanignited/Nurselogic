import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='cp1252') as f:
    c = f.read()

# Replace any literal 'Ã©' with '&eacute;' and 'Ã³' with '&oacute;' and 'Ã\xad' with '&iacute;'
c = c.replace('Ã©', '&eacute;')
c = c.replace('Ã³', '&oacute;')
c = c.replace('Ã\xad', '&iacute;')
c = c.replace('Ã¡', '&aacute;')
c = c.replace('Ãº', '&uacute;')
c = c.replace('Ã±', '&ntilde;')
c = c.replace('Ã', '&Aacute;') # Fallback for random Ã
# Wait, let's just do standard Spanish fixes
c = c.replace('Médico', 'M&eacute;dico')
c = c.replace('médico', 'm&eacute;dico')
c = c.replace('Admisión', 'Admisi&oacute;n')
c = c.replace('Evaluación', 'Evaluaci&oacute;n')
c = c.replace('Antropométrica', 'Antropom&eacute;trica')
c = c.replace('Clínicos', 'Cl&iacute;nicos')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='cp1252') as f:
    f.write(c)

print('Cleaned up accents in dashboard')
