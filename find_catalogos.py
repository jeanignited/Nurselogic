import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('abrirModalCatalogos')
print("abrirModalCatalogos at:", idx)

idx2 = c.find('verFichaClinica')
print("verFichaClinica at:", idx2)
