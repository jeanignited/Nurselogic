with open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'listaCitas' in line:
        for j in range(max(0, i-2), min(len(lines), i+15)):
            if j < len(lines):
                print(lines[j].strip())
        print("----")
        break
