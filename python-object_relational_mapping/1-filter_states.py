#!/usr/bin/python3
"""List all states with a name starting with N (uppercase N)"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit()
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
