import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = """function mostrarAlertaSoporte() {
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)',
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}
</script>"""

c = c.replace("</script>", new_js)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated scripts.jsp")
