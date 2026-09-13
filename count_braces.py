import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

# find first script block
idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js_code = text[idx_start:idx_end]

# count braces
open_braces = js_code.count('{')
close_braces = js_code.count('}')
print(f"Braces: {open_braces} open, {close_braces} close. Diff = {open_braces - close_braces}")
