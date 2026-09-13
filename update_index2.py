import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_str = '<canvas id="globalParticles" class="position-fixed w-100 h-100" style="top:0; left:0; z-index:-1; pointer-events: none; opacity: 0.6;"></canvas>'
new_str = old_str + '\n    <% if (isPaciente) { %>\n    <canvas id="pacienteParticles" class="position-fixed w-100 h-100" style="top:0; left:0; z-index:-1; pointer-events: none; opacity: 0.6;"></canvas>\n    <% } %>'

if '<canvas id="pacienteParticles"' not in c:
    c = c.replace(old_str, new_str)
    with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added pacienteParticles to index.jsp")
else:
    print("pacienteParticles already in index.jsp")
