#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def main():
    # Get MySQL credentials from command-line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
