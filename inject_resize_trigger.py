import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

# Add a resize dispatch when changing view
c = c.replace("document.getElementById(idVista).classList.add('vista-activa');", "document.getElementById(idVista).classList.add('vista-activa');\n    window.dispatchEvent(new Event('resize'));")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='latin-1') as f:
    f.write(c)
print('Injected resize event trigger')
