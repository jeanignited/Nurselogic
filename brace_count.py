import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Strip JSP tags
import re
c = re.sub(r'<%.*?%>', '', c, flags=re.DOTALL)
c = re.sub(r'<%@.*?%>', '', c)

# Extract content between <script> and </script>
scripts = re.findall(r'<script>(.*?)</script>', c, flags=re.DOTALL)
for i, s in enumerate(scripts):
    open_braces = s.count('{')
    close_braces = s.count('}')
    print(f"Script {i}: {open_braces} open, {close_braces} close")
