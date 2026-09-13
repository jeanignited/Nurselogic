import io
with io.open('dashboard_dump.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines:", len(lines))
# print around line 6334 if it exists
if len(lines) > 6330:
    for i in range(6330, min(6340, len(lines))):
        print(f"{i}: {lines[i].strip()}")
