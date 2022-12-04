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
    selector.execute("SELECT * FROM states ORDER BY id ASC")
    for state in selector.fetchall():
        print(state)
    selector.close()
    database.close()
