#!/usr/bin/python3
"""
Takes a state name as argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This version is safe from SQL injection.

Usage:
    ./3-my_safe_filter_states.py <username> <password> <db_name> <state_name>
"""

import MySQLdb
import sys


def main():
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db_name,
        port=3306
    )
    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC"
    )
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
