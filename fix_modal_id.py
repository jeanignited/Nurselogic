import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace any modalCat... with modalCatalogos
c = c.replace('id="modalCat\u00E1logos"', 'id="modalCatalogos"')
c = c.replace('id="modalCat\u00F3logos"', 'id="modalCatalogos"') # in case of wrong accent
c = c.replace('onclick="cerrarModalCat\u00E1logos()"', 'onclick="cerrarModalCatalogos()"')
# Also standard characters if powershell swallowed accents
c = c.replace('id="modalCatlogos"', 'id="modalCatalogos"')
c = c.replace('onclick="cerrarModalCatlogos()"', 'onclick="cerrarModalCatalogos()"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    s = f.read()
s = s.replace('cerrarModalCat\u00E1logos', 'cerrarModalCatalogos')
with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(s)

print("Fixed modalCatalogos ID")
