import io
with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    for line in f:
        if 'Agenda' in line:
            print(line.strip())
