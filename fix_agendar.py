import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

func = '''function configurarMinFechaCita() {
            let input = document.getElementById('citaFechaHora');
            if (input) {
                let now = new Date();
                now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
                input.min = now.toISOString().slice(0, 16);
            }
        }
        
        function abrirModalCitaAdmin() {'''

c = c.replace('function abrirModalCitaAdmin() {', func)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added configurarMinFechaCita")
