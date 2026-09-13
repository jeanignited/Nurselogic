import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

# Let's fix specific words
c = re.sub(r'M.{1,3}dico', 'M&eacute;dico', c)
c = re.sub(r'M.{1,3}dica', 'M&eacute;dica', c)
c = re.sub(r'Admisi.{1,3}n', 'Admisi&oacute;n', c)
c = re.sub(r'Evaluaci.{1,3}n', 'Evaluaci&oacute;n', c)
c = re.sub(r'Antropom.{1,3}trica', 'Antropom&eacute;trica', c)
c = re.sub(r'Cl.{1,3}nicos', 'Cl&iacute;nicos', c)
c = re.sub(r'un .{1,3}rea m&eacute;dica', 'un &aacute;rea m&eacute;dica', c)
c = re.sub(r'Odontolog.{1,3}a', 'Odontolog&iacute;a', c)
c = re.sub(r'Pediatr.{1,3}a', 'Pediatr&iacute;a', c)
c = re.sub(r'Ginecolog.{1,3}a', 'Ginecolog&iacute;a', c)
c = re.sub(r'Presi.{1,3}n', 'Presi&oacute;n', c)
c = re.sub(r'', '&deg;', c) # For temperature C

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed encoding issues in dashboard.jsp')
