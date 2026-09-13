import sqlite3
import os

db_path = 'db_nurselogic.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT precio FROM medicamentos LIMIT 1")
    print(cur.fetchone())
else:
    print('DB not found')
