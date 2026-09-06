import re
with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract content between <script> and </script>
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
with open('test_syntax.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(scripts))
