import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('onclick="window.print()"', 'onclick="imprimirFactura()"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated modals.jsp to use imprimirFactura')
