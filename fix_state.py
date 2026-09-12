import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add to cambiarVista
c = c.replace('changingActiveNav(vistaId);', "sessionStorage.setItem('ultima_vista_nurselogic', vistaId);\n            changingActiveNav(vistaId);")

# Update DOMContentLoaded
old_init = '''        var urlParams = new URLSearchParams(window.location.search);
        var vista = urlParams.get('vista');
        if (vista) {
            cambiarVista(vista);
        }
    } catch(e) {}'''

new_init = '''        var urlParams = new URLSearchParams(window.location.search);
        var vista = urlParams.get('vista');
        if (vista) {
            cambiarVista(vista);
        } else {
            var ultimaVista = sessionStorage.getItem('ultima_vista_nurselogic');
            if (ultimaVista) {
                cambiarVista(ultimaVista);
            }
        }
    } catch(e) {}'''

c = c.replace(old_init, new_init)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Modified scripts.jsp")
