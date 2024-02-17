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
            SELECT * FROM states WHERE name LIKE BINARY %(name)s \
ORDER BY states.id ASC""", {'name': argv[4]})

        rows = csr.fetchall()

    for row in rows:
        print(row)
