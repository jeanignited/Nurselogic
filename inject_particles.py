import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

particles_js = '''
// Particles Animation
function initDashboardParticles() {
    const canvas = document.getElementById('dashboardParticles');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let width = canvas.width = canvas.offsetWidth;
    let height = canvas.height = canvas.offsetHeight;
    let particles = [];
    
    window.addEventListener('resize', () => {
        if(canvas.offsetWidth === 0) return;
        width = canvas.width = canvas.offsetWidth;
        height = canvas.height = canvas.offsetHeight;
    });

    for (let i = 0; i < 40; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2.5 + 1,
            dx: (Math.random() - 0.5) * 0.5,
            dy: (Math.random() - 0.5) * 0.5,
            alpha: Math.random() * 0.5 + 0.1
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
            ctx.fillStyle = gba(56, 189, 248, ); // Cyan color
            ctx.fill();
        });
    }
    animate();
}

document.addEventListener('DOMContentLoaded', initDashboardParticles);
'''

c = c.replace('</script>', particles_js + '\n</script>')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='latin-1') as f:
    f.write(c)
print('Injected particles js')
