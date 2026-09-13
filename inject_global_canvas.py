import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

global_canvas = '''<body>
    <canvas id="globalParticles" class="position-fixed w-100 h-100" style="top:0; left:0; z-index:-1; pointer-events: none; opacity: 0.6;"></canvas>
'''
c = c.replace('<body>', global_canvas)

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Injected globalParticles into index.jsp')
