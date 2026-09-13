import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will wrap the patient dashboard in <div id="vista-inicio">
pattern = r'(<div id="dashboard_paciente" class="vista-activa">)(\s*<)'
c = re.sub(pattern, r'\1\n        <div id="vista-inicio">\2', c)

# And close it right before <% } %>
pattern2 = r'(</div>\s*</div>\s*</div>\s*</div>)\s*(<% } %>)'
# wait, how many divs close dashboard_paciente?
