import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

js_func = '''
window.imprimirFactura = function() {
    var id = document.getElementById('verFacId').innerText;
    var cliente = document.getElementById('verFacCliente').innerText;
    var fecha = document.getElementById('verFacFecha').innerText;
    var detalles = document.getElementById('verFacDetalles').innerHTML;
    var total = document.getElementById('verFacTotal').innerText;
    
    var w = window.open('', '', 'width=800,height=600');
    w.document.write('<html><head><title>Factura ' + id + '</title>');
    w.document.write('<style>body{font-family:sans-serif;padding:20px;} .factura-box{border:1px solid #ccc;padding:20px;} .header{text-align:center;} .tot{text-align:right;font-size:1.2em;font-weight:bold;}</style>');
    w.document.write('</head><body><div class="factura-box"><div class="header"><h2>Farmacia NurseLogic</h2><h3>Factura ' + id + '</h3></div>');
    w.document.write('<p><strong>Cliente:</strong> ' + cliente + '</p>');
    w.document.write('<p><strong>Fecha:</strong> ' + fecha + '</p><hr>');
    w.document.write('<div>' + detalles + '</div><hr>');
    w.document.write('<p class="tot">TOTAL: $' + total + '</p>');
    w.document.write('</div><script>window.print();</script></body></html>');
    w.document.close();
};
'''
if 'imprimirFactura' not in c:
    c = c + js_func
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
print('Added imprimirFactura to scripts.jsp')
