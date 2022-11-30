import sqlite3
from zk import ZK, const


zk = ZK('192.168.1.201')
conn = zk.connect()
attendance = conn.get_attendance()
print (type(attendance))
