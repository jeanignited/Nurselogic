import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function confirmarBorrado(')
print("confirmarBorrado at", idx)

idx_script1 = c.find('<script>')
print("first <script> at", idx_script1)

idx_script_end1 = c.find('</script>', idx_script1+1)
print("first </script> at", idx_script_end1)

idx_script2 = c.find('<script>', idx_script1+1)
print("second <script> at", idx_script2)
