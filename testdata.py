import sqlite3



con= sqlite3.connect('data.bd')
cur= con.cursor
cur.execute('''CREATE TABLE IF NOT EXISTS
            ( name TEXT,
            number TEXT
                ''')
cur.execute('''INSERT INTO tables('raha','12876543')''')
con.commit
