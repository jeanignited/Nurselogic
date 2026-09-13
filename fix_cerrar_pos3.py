import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# First, restore the original <script src="..."> tag
bad_script = '''<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js">
window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};
</script>'''

c = c.replace(bad_script, '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>')

func = '''
window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};
'''

# Now inject it before the final </script>
# Find the LAST </script>
idx = c.rfind('</script>')
if idx != -1:
    c = c[:idx] + func + c[idx:]

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed script injection properly")
