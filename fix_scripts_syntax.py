import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will use a robust regex to replace everything between ctx.beginPath() and ctx.fill()
pattern = r'ctx\.beginPath\(\);\s*ctx\.arc\(p\.x, p\.y, p\.radius, 0, Math\.PI \* 2\);.*?ctx\.fill\(\);'
replacement = '''ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light';
            let r = isLight ? 59 : 56;
            let g = isLight ? 130 : 189;
            let b = isLight ? 246 : 248;
            ctx.fillStyle = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + p.alpha + ')';
            ctx.fill();'''

c = re.sub(pattern, replacement, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed syntax error in scripts.jsp')
