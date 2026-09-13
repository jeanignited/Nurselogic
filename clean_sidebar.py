import io

with io.open('src/main/webapp/includes/sidebar.jsp', 'rb') as f:
    raw = f.read()

c = raw.decode('utf-8', errors='replace')
c = c.replace(u'M\u00c3\u00a9dico', u'M&eacute;dico')
c = c.replace(u'M\u00c3\u00a9dica', u'M&eacute;dica')
c = c.replace(u'M\ufffddica', u'M&eacute;dica')
c = c.replace(u'Hospitalizaci\u00c3\u00b3n', u'Hospitalizaci&oacute;n')
c = c.replace(u'Hospitalizaci\ufffd\ufffdn', u'Hospitalizaci&oacute;n')
c = c.replace(u'Hospitalizaci\ufffdn', u'Hospitalizaci&oacute;n')
c = c.replace(u'Estad\u00c3\u00adsticas', u'Estad&iacute;sticas')
c = c.replace(u'Estad\ufffdsticas', u'Estad&iacute;sticas')
c = c.replace(u'F\u00c3\u00a1rmacos', u'F&aacute;rmacos')
c = c.replace(u'F\ufffdrmacos', u'F&aacute;rmacos')
c = c.replace(u'Cat\u00c3\u00a1logos', u'Cat&aacute;logos')
c = c.replace(u'Cat\ufffdlogos', u'Cat&aacute;logos')
c = c.replace(u'Cl\u00c3\u00adnicos', u'Cl&iacute;nicos')
c = c.replace(u'Cl\ufffdnicos', u'Cl&iacute;nicos')
c = c.replace(u'Sesi\u00c3\u00b3n', u'Sesi&oacute;n')
c = c.replace(u'Sesi\ufffdn', u'Sesi&oacute;n')

with io.open('src/main/webapp/includes/sidebar.jsp', 'wb') as f:
    f.write(c.encode('utf-8'))

print('Cleaned sidebar.jsp')
