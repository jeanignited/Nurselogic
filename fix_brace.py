import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will find the function and remove the extra brace.
old_block = '''            }
        }



        }'''
new_block = '''            }
        }'''

c = c.replace(old_block, new_block)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Extra brace removed.")
