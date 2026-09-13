import io
import subprocess

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find first script block
idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js_code = text[idx_start:idx_end]

with io.open('temp_test.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Saved temp_test.js")
