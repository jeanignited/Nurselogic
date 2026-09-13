# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(13, 110, 253, 0.05);"', 'style="background-color: rgba(13, 110, 253, 0.05); border: none;"')
c = c.replace('style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(255, 193, 7, 0.05);"', 'style="background-color: rgba(255, 193, 7, 0.05); border: none;"')
c = c.replace('style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(220, 53, 69, 0.05);"', 'style="background-color: rgba(220, 53, 69, 0.05); border: none;"')
c = c.replace('style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(25, 135, 84, 0.05);"', 'style="background-color: rgba(25, 135, 84, 0.05); border: none;"')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Vitals cards styles successfully replaced.")
