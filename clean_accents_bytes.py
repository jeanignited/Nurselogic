import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'rb') as f:
    raw = f.read()

# Decode as utf-8, replace bad bytes
c = raw.decode('utf-8', errors='replace')

# Replace exact strings that are corrupted
c = c.replace(u'M\ufffd\ufffddico', u'M&eacute;dico')
c = c.replace(u'M\ufffd\ufffddica', u'M&eacute;dica')
c = c.replace(u'M\ufffddico', u'M&eacute;dico')
c = c.replace(u'M\ufffddica', u'M&eacute;dica')
c = c.replace(u'Admisi\ufffd\ufffdn', u'Admisi&oacute;n')
c = c.replace(u'Admisi\ufffdn', u'Admisi&oacute;n')
c = c.replace(u'Evaluaci\ufffd\ufffdn', u'Evaluaci&oacute;n')
c = c.replace(u'Evaluaci\ufffdn', u'Evaluaci&oacute;n')
c = c.replace(u'Antropom\ufffd\ufffdtrica', u'Antropom&eacute;trica')
c = c.replace(u'Antropom\ufffdtrica', u'Antropom&eacute;trica')
c = c.replace(u'Cl\ufffd\ufffdnicos', u'Cl&iacute;nicos')
c = c.replace(u'Cl\ufffdnicos', u'Cl&iacute;nicos')
c = c.replace(u'\ufffd\ufffdrea', u'&aacute;rea')
c = c.replace(u'\ufffdrea', u'&aacute;rea')
c = c.replace(u'Odontolog\ufffd\ufffda', u'Odontolog&iacute;a')
c = c.replace(u'Odontolog\ufffda', u'Odontolog&iacute;a')
c = c.replace(u'Pediatr\ufffd\ufffda', u'Pediatr&iacute;a')
c = c.replace(u'Pediatr\ufffda', u'Pediatr&iacute;a')
c = c.replace(u'Ginecolog\ufffd\ufffda', u'Ginecolog&iacute;a')
c = c.replace(u'Ginecolog\ufffda', u'Ginecolog&iacute;a')
c = c.replace(u'Presi\ufffd\ufffdn', u'Presi&oacute;n')
c = c.replace(u'Presi\ufffdn', u'Presi&oacute;n')
c = c.replace(u'M\u00e9dico', u'M&eacute;dico')
c = c.replace(u'M\u00e9dica', u'M&eacute;dica')

# And handle the literal string from the image if it is UTF-8 decoded double
c = c.replace(u'M\u00c3\u00a9dico', u'M&eacute;dico')
c = c.replace(u'M\u00c3\u00a9dica', u'M&eacute;dica')
c = c.replace(u'Admisi\u00c3\u00b3n', u'Admisi&oacute;n')
c = c.replace(u'Evaluaci\u00c3\u00b3n', u'Evaluaci&oacute;n')

with io.open('src/main/webapp/views/dashboard.jsp', 'wb') as f:
    f.write(c.encode('utf-8'))

print('Cleaned up accents aggressively using bytes')
