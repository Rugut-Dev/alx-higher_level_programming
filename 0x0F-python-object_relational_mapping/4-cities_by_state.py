#!/usr/bin/python3
"""
script thaT lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        db=argv[3],
        passwd="password"
        )

    with db.cursor() as csr:
        csr.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)
        rows = csr.fetchall()

    for row in rows:
        print(row)
