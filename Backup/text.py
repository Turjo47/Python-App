import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("""CREATE TABLE if not exists data( id INTEGER PRIMARY KEY, Ip TEXT ,Port TEXT, Api Text, Status Integer)""")
cur.execute("DELETE FROM data WHERE id=1")