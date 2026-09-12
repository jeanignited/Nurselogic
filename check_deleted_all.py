import io, os

words = [b'Clnica', b'aos', b'Antropomtrica', b'Evaluacin', b'Observacin']

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            with io.open(os.path.join(root, file), 'rb') as f:
                c = f.read()
            for w in words:
                if w in c:
                    print(f"Found {w} in {file}")
