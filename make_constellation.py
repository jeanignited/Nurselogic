import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will replace the animate() loop in scripts.jsp to include line drawing between particles!
new_animate = '''    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, width, height);
        
        let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light';
        let r = isLight ? 59 : 56;
        let g = isLight ? 130 : 189;
        let b = isLight ? 246 : 248;

        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];
            p.x += p.dx;
            p.y += p.dy;
            if (p.x < 0 || p.x > width) p.dx = -p.dx;
            if (p.y < 0 || p.y > height) p.dy = -p.dy;
            
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + p.alpha + ')';
            ctx.fill();
            
            // Draw connecting lines
            for (let j = i + 1; j < particles.length; j++) {
                let p2 = particles[j];
                let dist = Math.sqrt(Math.pow(p.x - p2.x, 2) + Math.pow(p.y - p2.y, 2));
                if (dist < 120) {
                    ctx.beginPath();
                    ctx.strokeStyle = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + (0.2 - dist/600) + ')';
                    ctx.lineWidth = 1;
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.stroke();
                }
            }
        }
    }'''

pattern = r'function animate\(\) \{.*?\}\s*animate\(\);'
c = re.sub(pattern, new_animate + '\n    animate();', c, flags=re.DOTALL)

# increase particles to 120
c = c.replace('for (let i = 0; i < 70; i++)', 'for (let i = 0; i < 120; i++)')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated particles to have connecting lines (constellation effect)')
