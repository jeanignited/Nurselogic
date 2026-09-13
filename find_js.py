import os
for root, dirs, files in os.walk('src/main/webapp'):
    for f in files:
        if f.endswith('.js'):
            print(os.path.join(root, f))
