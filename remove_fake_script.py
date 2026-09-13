import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

script_to_remove = '''<script>
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

c = c.replace(script_to_remove, '')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Removed fake cambiarVista from index.jsp")
