#!/usr/bin/python3
"""List all cities of a state passed as argument (safe from SQL injection)"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit()
    user, passwd, db, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    conn.close()
