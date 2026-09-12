import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Extract script content
m = re.search(r'<script>(.*?)</script>', c, re.DOTALL)
if m:
    with io.open('check_syntax.js', 'w', encoding='utf-8') as f:
        f.write(m.group(1))
    print("Extracted to check_syntax.js")
