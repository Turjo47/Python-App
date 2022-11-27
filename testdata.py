import sqlite3
con= sqlite3.connect('data.bd')
cur= con.cursor()
cur.execute("""CREATE TABLE tables(
            name TEXT,
            number TEXT)
            """)
cur.execute("INSERT INTO tables VALUES('raha','12876543')")
cur.execute("SELECT rowid,* FROM tables")
items= cur.fetchall()
for item in items:
    print (item)
con.commit()
con.close()