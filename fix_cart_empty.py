import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = '''
window.vaciarCarrito = function() {
    carritoVentas = [];
    document.getElementById('cartBubbleContainer').classList.add('d-none');
    var mEl = document.getElementById('modalCarrito');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }
};
'''

c = c.replace('let carritoVentas = [];', 'let carritoVentas = [];' + new_js)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added vaciarCarrito")
