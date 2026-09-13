with open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    for line in f:
        if 'setAttribute' in line:
            print(line.strip())
