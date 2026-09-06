
        function mostrarPanel(idPanel) {
            document.querySelectorAll('.panel').forEach(el => el.classList.add('d-none'));
            document.getElementById(idPanel).classList.remove('d-none');
        }

        function setTheme(theme) {
            localStorage.setItem('nurselogic_theme', theme);
            applyTheme(theme);
        }

        function applyTheme(theme) {
            let actualTheme = theme;
            if (theme === 'auto') {
                actualTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            }
            document.documentElement.setAttribute('data-theme', actualTheme);

            let iconLogin = document.getElementById('themeIconLogin');
            let labelLogin = document.getElementById('themeLabelLogin');
            let iconClass = 'bi-moon-stars-fill';
            let labelText = 'Oscuro';
            if (theme === 'light') { iconClass = 'bi-sun-fill'; labelText = 'Claro'; }
            else if (theme === 'auto') { iconClass = 'bi-display'; labelText = 'Auto'; }

            if (iconLogin) iconLogin.className = 'bi ' + iconClass;
            if (labelLogin) labelLogin.innerText = labelText;
        }

        (function() {
            let savedTheme = localStorage.getItem('nurselogic_theme') || 'auto';
            applyTheme(savedTheme);
            window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', e => {
                if (localStorage.getItem('nurselogic_theme') === 'auto') {
                    applyTheme('auto');
                }
            });
        })();
    
