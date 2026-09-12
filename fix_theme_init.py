import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add a script tag in the head to initialize the theme from localStorage
theme_init_script = '''
    <script>
        (function() {
            var theme = localStorage.getItem('nurselogic_theme') || 'dark';
            var actualTheme = theme;
            if (theme === 'auto') {
                actualTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            }
            document.documentElement.setAttribute('data-bs-theme', actualTheme);
        })();
    </script>
'''

c = c.replace('</head>', theme_init_script + '</head>')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
