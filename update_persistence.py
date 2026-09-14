import io
with io.open('src/main/resources/META-INF/persistence.xml', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('jdbc:mysql://localhost:3306/nurselogic_db?useSSL=false&amp;serverTimezone=UTC', 'jdbc:mysql://localhost:3306/nurselogic_db?useSSL=false&amp;serverTimezone=UTC&amp;useUnicode=true&amp;characterEncoding=UTF-8')

with io.open('src/main/resources/META-INF/persistence.xml', 'w', encoding='utf-8') as f:
    f.write(c)
