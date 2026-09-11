import io, re
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()
c = c.replace('id="modalCat\xe1logos"', 'id="modalCatalogos"')
c = c.replace('cerrarModalCat\xe1logos()', 'cerrarModalCatalogos()')
c = c.replace('id="formEnfermedad"', 'id="catEnfermedadCampos"')
c = c.replace('id="formAlergia"', 'id="catAlergiaCampos"')
with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
