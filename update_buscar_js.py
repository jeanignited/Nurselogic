import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

js_func = '''
window.buscarClienteCarrito = function(cedula) {
    if (cedula.length === 10) {
        fetch("adminAction?action=buscarClienteCedula&cedula=" + cedula)
            .then(r => r.json())
            .then(data => {
                let input = document.getElementById("ventaClienteCarrito");
                if (data.nombre) {
                    input.value = data.nombre;
                    input.classList.add("fw-bold", "text-info");
                }
            }).catch(e => console.log(e));
    }
};
'''
if 'buscarClienteCarrito' not in c:
    c = c + js_func
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
print('Added buscarClienteCarrito to scripts.jsp')
