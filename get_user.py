# -*- coding: utf-8 -*-
import sys
sys.path.append("zk")

from zk import ZK, const
ip = sys.argv[1]
port= sys.argv[2]
print(port)
conn = None
zk = ZK(ip ='192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    # print ('Connecting to device ...')
    conn = zk.connect()

    records = conn.get_users()
    for record in records:
        print(record)
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
