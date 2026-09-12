import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("let iconNav = document.getElementById('themeIcon');", "let iconNav = document.getElementById('themeIconDash');")
c = c.replace("let labelNav = document.getElementById('themeLabel');", "let labelNav = document.getElementById('themeLabelDash');")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

