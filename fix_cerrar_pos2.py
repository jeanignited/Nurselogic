import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Find window.cerrarModalCatalogos after </script>
idx = c.find('</script>')
if idx != -1:
    after_script = c[idx + 9:]
    if 'cerrarModalCatalogos' in after_script:
        c = c[:idx + 9] # strip everything after </script>
        
        # Now insert the function before </script>
        func = '''
window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};
'''
        c = c.replace('</script>', func + '</script>')
        
        with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Fixed cerrarModalCatalogos location")
    else:
        print("Not found after </script>")
