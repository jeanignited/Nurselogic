import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

c = c.replace("getElementById('dashboardParticles')", "getElementById('globalParticles')")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='latin-1') as f:
    f.write(c)
print('Updated scripts.jsp to target globalParticles')
