import io

def fix_encoding(filepath):
    try:
        with io.open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # If it has double encoded utf-8
        # example: é is C3 A9
        # encode it back to windows-1252 to get the raw bytes, then decode as utf-8
        
        # But wait! I might have written normal characters too (like the Swal.fire code).
        # If I convert EVERYTHING back, my newly added Swal.fire code (which has \xbf and \xed) 
        # might break if it wasn't double-encoded.
        pass
    except Exception as e:
        print(e)

s = "Cédula"
print(s.encode('windows-1252').decode('utf-8'))
