#!/usr/bin/python3
"""
Takes a state name as argument and displays all values in the states table
where name matches the argument (case-sensitive match).
Usage: ./2-my_filter_states.py <username> <password> <db_name> <state_name>
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

    # SQL injection-prone way required by the project (but with LIKE BINARY for case sensitivity)
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"\
        .format(state_name)
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
