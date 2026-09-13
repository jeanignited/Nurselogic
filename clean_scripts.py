import io

with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    raw = f.read()

c = raw.decode('utf-8', errors='replace')
c = c.replace(u'\u00c3\u00a1', u'&aacute;')
c = c.replace(u'\u00c3\u00a9', u'&eacute;')
c = c.replace(u'\u00c3\u00ad', u'&iacute;')
c = c.replace(u'\u00c3\u00b3', u'&oacute;')
c = c.replace(u'\u00c3\u00ba', u'&uacute;')
c = c.replace(u'\u00c3\u00b1', u'&ntilde;')
c = c.replace(u'\u00c3\u0081', u'&Aacute;')
c = c.replace(u'\u00c3\u0089', u'&Eacute;')
c = c.replace(u'\u00c3\u008d', u'&Iacute;')
c = c.replace(u'\u00c3\u0093', u'&Oacute;')
c = c.replace(u'\u00c3\u009a', u'&Uacute;')
c = c.replace(u'\u00c3\u0091', u'&Ntilde;')
# In JS, HTML entities are NOT decoded in alert boxes! We should use unicode escapes for alert boxes or standard JS characters.
# Actually, since it's UTF-8 now, let's just convert them to standard letters!
c = c.replace(u'&aacute;', u'\u00e1')
c = c.replace(u'&eacute;', u'\u00e9')
c = c.replace(u'&iacute;', u'\u00ed')
c = c.replace(u'&oacute;', u'\u00f3')
c = c.replace(u'&uacute;', u'\u00fa')
c = c.replace(u'&ntilde;', u'\u00f1')

with io.open('src/main/webapp/includes/scripts.jsp', 'wb') as f:
    f.write(c.encode('utf-8'))

print('Cleaned scripts.jsp')
