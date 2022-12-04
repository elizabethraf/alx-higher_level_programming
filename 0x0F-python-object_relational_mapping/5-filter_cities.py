#!/usr/bin/python3
"""
Lists of all states from the database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect("localhost",
                               sys.argv[1], sys.argv[2], sys.argv[3])
    query = "SELECT cities.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id\
            WHERE cities.state_id = %s"

    selector = database.cursor()
    selector.execute(query, sys.argv[4])
    cities = {}
    for city in selector.fetchall():
        print(", ".join(cities)))
    selector.close()
    database.close()
