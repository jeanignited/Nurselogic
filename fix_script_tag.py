import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the existing </script>
c = c.replace('</script>', '')

# Append it at the end
c = c + '\n</script>\n'

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed scripts.jsp script tag')
