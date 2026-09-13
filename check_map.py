with open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'map.put("estado"' in line:
        for j in range(i-2, i+30):
            if j < len(lines):
                print(lines[j].strip())
        break
