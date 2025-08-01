#!/usr/bin/python3
"""
Lists all states with names starting with 'N' (uppercase N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def main():
    # Get credentials
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db_name,
        port=3306
    )

    cur = db.cursor()

    # Select states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
