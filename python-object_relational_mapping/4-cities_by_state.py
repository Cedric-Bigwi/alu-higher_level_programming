#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit()
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    query = """SELECT cities.id, cities.name, states.name 
               FROM cities 
               JOIN states ON cities.state_id = states.id 
               ORDER BY cities.id ASC"""
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
