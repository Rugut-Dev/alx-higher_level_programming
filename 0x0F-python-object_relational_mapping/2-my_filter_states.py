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

    csr = db.cursor()
    csr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
 ORDER BY states.id ASC".format(argv[4]))
    rows = csr.fetchall()

    for row in rows:
        print(row)
