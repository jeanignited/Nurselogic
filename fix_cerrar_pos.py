import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

bad_append = '''</script>

window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};'''

good_append = '''
window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};
</script>
'''

c = c.replace(bad_append, good_append)
c = c.replace('</script>\nwindow.cerrarModalCatalogos', 'window.cerrarModalCatalogos') # Just in case whitespace differs

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Moved cerrarModalCatalogos inside <script>")
