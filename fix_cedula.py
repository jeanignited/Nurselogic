import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_block = "document.getElementById('cedulaBusqueda').addEventListener('keyup', function() {"
new_block = "let cb = document.getElementById('cedulaBusqueda');\n        if (cb) cb.addEventListener('keyup', function() {"

c = c.replace(old_block, new_block)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Replaced cedulaBusqueda listener")
