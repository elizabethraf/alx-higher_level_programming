#!/usr/bin/python3
"""
Lists of all states from the database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect("localhost",
                               sys.argv[1], sys.argv[2], sys.argv[3])

    selector = database.cursor()
    selector.execute("""
    SELECT id, name
    FROM
    states
    WHERE
    name = %(state_name)s
    ORDER BY
    states.id ASC
    """, {
        'state_name': sys.argv[4]
        }
    )
    for state in selector.fetchall():
        print(state)
    selector.close()
    database.close()
