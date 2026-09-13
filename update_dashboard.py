# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add the canvas
old_container = '<div id="dashboard_paciente" class="vista-activa">'
new_container = '''<div id="dashboard_paciente" class="vista-activa position-relative" style="z-index: 10;">
        <canvas id="pacienteParticles" class="position-fixed w-100 h-100" style="top: 0; left: 0; z-index: -1; pointer-events: none; opacity: 0.6;"></canvas>'''

c = c.replace(old_container, new_container)

# Add the CSS for views
c = c.replace('<div id="vista-inicio">', '<div id="vista-inicio" class="position-relative" style="z-index: 10;">')
c = c.replace('<div id="vista-citas" class="d-none">', '<div id="vista-citas" class="d-none position-relative" style="z-index: 10;">')
c = c.replace('<div id="vista-resultados" class="d-none">', '<div id="vista-resultados" class="d-none position-relative" style="z-index: 10;">')
c = c.replace('<div id="vista-recetas" class="d-none">', '<div id="vista-recetas" class="d-none position-relative" style="z-index: 10;">')

# Add the script at the end of the patient block
script_injection = '''
        <script>
            function initPacienteParticles() {
                const canvas = document.getElementById('pacienteParticles');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                let width = canvas.width = window.innerWidth;
                let height = canvas.height = window.innerHeight;
                let particles = [];
                
                window.addEventListener('resize', () => {
                    if(window.innerWidth === 0) return;
                    width = canvas.width = window.innerWidth;
                    height = canvas.height = window.innerHeight;
                });

                for (let i = 0; i < 70; i++) {
                    particles.push({
                        x: Math.random() * width,
                        y: Math.random() * height,
                        radius: Math.random() * 4 + 1.5,
                        dx: (Math.random() - 0.5) * 0.5,
                        dy: (Math.random() - 0.5) * 0.5
                    });
                }

                function animate() {
                    requestAnimationFrame(animate);
                    ctx.clearRect(0, 0, width, height);
                    particles.forEach(p => {
                        p.x += p.dx;
                        p.y += p.dy;
                        if (p.x < 0 || p.x > width) p.dx = -p.dx;
                        if (p.y < 0 || p.y > height) p.dy = -p.dy;
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                        ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
                        ctx.fill();
                    });
                }
                animate();
            }
            document.addEventListener("DOMContentLoaded", initPacienteParticles);
        </script>
<% } %>'''

idx = c.rfind('<% } %>')
if idx != -1:
    c = c[:idx] + script_injection + c[idx+7:]

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Dashboard patient view updated with particles")
