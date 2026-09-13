import io

# Remove from dashboard.jsp
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('''
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
''', '')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

# Add to index.jsp
with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    idx = f.read()

script_to_inject = '''<script>
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

idx = idx.replace('</body>', script_to_inject + '</body>')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Moved script to index.jsp before </body>")
