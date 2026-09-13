import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("document.getElementById('tbodyCarrito')", "document.getElementById('tablaCarritoCuerpo')")
c = c.replace("document.getElementById('carritoTotal')", "document.getElementById('carritoTotalLabel')")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed carrito element IDs")
