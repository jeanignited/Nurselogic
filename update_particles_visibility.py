import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace particle settings
# From: radius: Math.random() * 2.5 + 1
# To: radius: Math.random() * 4 + 1.5
c = re.sub(r'radius: Math\.random\(\) \* 2\.5 \+ 1', 'radius: Math.random() * 4 + 1.5', c)

# From: alpha: Math.random() * 0.5 + 0.1
# To: alpha: Math.random() * 0.6 + 0.2
c = re.sub(r'alpha: Math\.random\(\) \* 0\.5 \+ 0\.1', 'alpha: Math.random() * 0.6 + 0.2', c)

# From: for (let i = 0; i < 40; i++)
# To: for (let i = 0; i < 70; i++)
c = re.sub(r'for \(let i = 0; i < 40; i\+\+\)', 'for (let i = 0; i < 70; i++)', c)

# From: ctx.fillStyle = 'rgba(56, 189, 248, ' + p.alpha + ')';
# To check theme and set color appropriately, but we can just use a darker blue or dynamic. 
# Let's use a function to get the current theme color. Actually, checking if the html has data-bs-theme="light" is easiest.
dynamic_color = '''
            let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light';
            let r = isLight ? 59 : 56;
            let g = isLight ? 130 : 189;
            let b = isLight ? 246 : 248;
            ctx.fillStyle = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + p.alpha + ')';
'''
c = re.sub(r"ctx\.fillStyle = 'rgba\(56, 189, 248, ' \+ p\.alpha \+ '\)';", dynamic_color.strip(), c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated particles settings for better visibility and light mode support')
