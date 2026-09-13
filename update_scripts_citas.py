import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_script = '''
window.exportarCitasFechas = function() {
    let today = new Date().toISOString().split('T')[0];
    Swal.fire({
        title: 'Exportar Agenda M\xe9dica',
        html: '<div class="text-start">' +
              '<label class="form-label small text-secondary">Desde:</label>' +
              '<input type="date" id="expCitasDesde" class="form-control mb-3 bg-transparent text-white border-secondary" max="' + today + '">' +
              '<label class="form-label small text-secondary">Hasta:</label>' +
              '<input type="date" id="expCitasHasta" class="form-control bg-transparent text-white border-secondary" max="' + today + '">' +
              '</div>',
        background: 'var(--bg-panel)', color: 'var(--text-color)',
        showCancelButton: true, confirmButtonText: 'Exportar', cancelButtonText: 'Cancelar'
    }).then(res => {
        if (res.isConfirmed) {
            let d = document.getElementById('expCitasDesde').value;
            let h = document.getElementById('expCitasHasta').value;
            window.location.href = "exportCsv?tipo=citas&desde=" + d + "&hasta=" + h;
        }
    });
};
'''

# append right before </script>
c = c.replace('</script>', new_script + '\n</script>')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Added exportarCitasFechas to scripts.jsp')
