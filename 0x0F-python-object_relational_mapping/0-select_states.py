#!/usr/bin/python3
"""
Lists of all states from the database.

"""


import sys
import MySQLdb


if __name__ == '__main__':
    database = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2],
            sys.argv[3])

    selector = database.cursor()
    selector.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    selector.close()
    database.close()
