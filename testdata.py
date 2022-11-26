import sqlite3



con= sqlite3.connect('data.bd')
cur= con.cursor
cur.execute('''CREATE TABLE IF NOT EXISTS
            ( name TEXT,
            number TEXT
                ''')
cur.execute('''INSERT INTO tables('turjo','1235235151')''')
con.commit
