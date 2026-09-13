import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's find dashboard_paciente
start_idx = c.find('<div id="dashboard_paciente"')
end_idx = c.rfind('<% } %>', 0, len(c))
print(c[end_idx-200:end_idx+20])
