with open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'public ActionResult prescribirReceta' in line:
        for j in range(i+65, i+95):
            if j < len(lines):
                print(lines[j].strip())
        break
