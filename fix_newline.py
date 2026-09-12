import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('\\n    <style>', '\n    <style>')
c = c.replace('\\n<jsp:include', '\n<jsp:include')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
