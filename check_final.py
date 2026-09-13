import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

lines = js.split('\n')
for i, line in enumerate(lines):
    if line.strip().startswith('<') and not line.strip().startswith('<%'):
        print(f"Naked HTML starting with < at line {i}: {line}")
        
js_no_jsp = re.sub(r'<%.*?%>', '', js, flags=re.DOTALL)
print(f"Braces in JS only: {js_no_jsp.count('{')} open, {js_no_jsp.count('}')} close")
