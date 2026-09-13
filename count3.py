import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

# remove comments
js = re.sub(r'//.*', '', js)
js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)

# Let's count them naively, it might be fine
print(f"Braces: {js.count('{')} open, {js.count('}')} close")
print(f"Parens: {js.count('(')} open, {js.count(')')} close")
