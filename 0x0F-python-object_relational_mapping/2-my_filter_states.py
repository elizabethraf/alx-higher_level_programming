#!/usr/bin/python3
"""
Lists of all states from the database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
    query = "SELECT id, name FROM states\
            WHERE name = '{}' COLLATE utf8_bin\
            ORDER BY states.id ASC".format(sys.argv[4])

    selector = database.cursor()
    selector.execute(query)
    for state in selector.fetchall():
        print(state)
    selector.close()
    database.close()
