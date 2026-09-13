import io
import re
from pyjsparser import parse

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

# we need to remove JSP tags to let pyjsparser parse it
# JS parser fails on <% ... %> so we replace them with empty strings
js = re.sub(r'<%=(.*?)%>', r'"\1"', js)
js = re.sub(r'<%(.*?)%>', r'', js, flags=re.DOTALL)

try:
    parse(js)
    print("JS Parsed successfully!")
except Exception as e:
    print("JS Syntax Error:", str(e))
