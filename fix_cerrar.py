import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_func = '''
window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};
'''
c = c + '\n' + new_func
with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    m = f.read()
m = m.replace('<button type="button" class="btn btn-secondary px-4" onclick="cerrarModalCatalogos()">Cancelar</button>', '')
with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(m)

print("Fixed cerrarModalCatalogos")
