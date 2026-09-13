with open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'public ActionResult atenderCita' in line:
        for j in range(i, i+30):
            if j < len(lines):
                print(lines[j].strip())
        break
