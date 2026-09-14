import io

with io.open('src/main/java/com/nurselogic/dao/UsuarioDAO.java', 'r', encoding='utf-8') as f:
    print(f.read())
