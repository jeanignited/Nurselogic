import os
for f in os.listdir('src/main/java/com/nurselogic/controller'):
    if f.endswith('.java'):
        with open('src/main/java/com/nurselogic/controller/' + f, 'r', encoding='utf-8') as file:
            content = file.read()
            if 'doPost' in content and 'setCharacterEncoding("UTF-8")' not in content:
                print("Missing in: " + f)
