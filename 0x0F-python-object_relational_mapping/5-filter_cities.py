#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd="password",
                         db=argv[3])
    with db.cursor() as csr:
        csr.execute("""
            SELECT cities.id, cities.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id ASC""", {'state_name': argv[4]})

        rows = csr.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
