import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# The theme_js was appended after </script>. Let's find </script> and move the appended code inside.
# Or simpler: we know the code starts with "// Lgica de Tema Claro / Oscuro"
# Let's wrap it in <script></script>

target = '// Lgica de Tema Claro / Oscuro'
if target in c:
    c = c.replace(target, '<script>\\n' + target)
    c = c + '\\n</script>'
    
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed scripts.jsp")
else:
    print("Target not found")

