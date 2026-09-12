import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

theme_js = '''
// Lgica de Tema Claro / Oscuro
function setTheme(theme) {
    localStorage.setItem('nurselogic_theme', theme);
    applyTheme(theme);
}

function applyTheme(theme) {
    let actualTheme = theme;
    if (theme === 'auto') {
        actualTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }
    document.documentElement.setAttribute('data-bs-theme', actualTheme);

    // Update icons if topbar has them
    let iconNav = document.getElementById('themeIcon');
    let labelNav = document.getElementById('themeLabel');
    let iconClass = 'bi-moon-stars-fill';
    let labelText = 'Oscuro';
    if (theme === 'light') { iconClass = 'bi-sun-fill text-warning'; labelText = 'Claro'; }
    else if (theme === 'auto') { iconClass = 'bi-display text-info'; labelText = 'Auto'; }

    if (iconNav) iconNav.className = 'bi ' + iconClass;
    if (labelNav) labelNav.innerText = labelText;
}

// Inicializar estado del dropdown si es que existe
document.addEventListener('DOMContentLoaded', function() {
    var savedTheme = localStorage.getItem('nurselogic_theme') || 'dark';
    applyTheme(savedTheme);
});
'''

c = c + theme_js

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
