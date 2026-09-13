import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

script_to_inject = '''
<script>
    function cambiarVista(idVista) {
        let todasLasVistas = document.querySelectorAll('div[id^="vista-"]');
        todasLasVistas.forEach(vista => {
            vista.classList.add('d-none');
        });
        let vistaDestino = document.getElementById(idVista);
        if(vistaDestino) {
            vistaDestino.classList.remove('d-none');
        }
    }
</script>
'''

c = c.rstrip() + '\n' + script_to_inject + '\n'

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Script injected at the end of dashboard.jsp")
