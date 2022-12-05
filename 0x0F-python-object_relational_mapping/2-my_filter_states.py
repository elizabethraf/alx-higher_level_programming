#!/usr/bin/python3
"""
Lists of all states from the database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect("localhost",
                               sys.argv[1], sys.argv[2], sys.argv[3])
    query = "SELECT id, name FROM states\
            WHERE name = '{}'".format(sys.argv[4])

    selector = database.cursor()
    selector.execute(query)
    for state in selector.fetchone():
        print(state)
    selector.close()
    database.close()
