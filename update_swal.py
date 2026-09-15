import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    scripts = f.read()

old_func = """function mostrarAlertaSoporte() {
    let isDark = document.body.classList.contains('dark-mode') || (document.documentElement.getAttribute('data-bs-theme') !== 'light' && document.documentElement.getAttribute('data-bs-theme') === 'dark');
    let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light' || (!isDark && !document.body.classList.contains('dark-mode'));
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: document.body.classList.contains('dark-mode') ? '#1e293b' : (isLight ? '#ffffff' : '#1e293b'),
        color: document.body.classList.contains('dark-mode') ? '#ffffff' : (isLight ? '#000000' : '#ffffff'),
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}"""

new_func = """function mostrarAlertaSoporte() {
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: document.body.classList.contains('dark-mode') ? '#1e293b' : '#ffffff',
        color: document.body.classList.contains('dark-mode') ? '#ffffff' : '#000000',
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}"""

if old_func in scripts:
    scripts = scripts.replace(old_func, new_func)
else:
    # Just in case
    scripts = re.sub(r'function mostrarAlertaSoporte\(\) \{[\s\S]*?\}\);[\s\n]*\}', new_func, scripts)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(scripts)
