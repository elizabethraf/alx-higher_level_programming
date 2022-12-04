#!/usr/bin/python3
"""
Lists of all states from the database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect("localhost",
                               sys.argv[1], sys.argv[2], sys.argv[3])
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY '{}'\
             ORDER BY states.id ASC.format(argv[4])"

    selector = database.cursor()
    selector.execute(query)
    for state in selector.fetchall():
        print(state)
    selector.close()
    database.close()
