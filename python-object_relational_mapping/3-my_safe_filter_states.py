#!/usr/bin/python3
"""List all states where name matches the argument (safe from SQL injection)"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit()
    user, passwd, db, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cur.execute(query, (name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
