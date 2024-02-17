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
    csr.execute("SELECT * FROM states ORDER BY states.id")
    rows = csr.fetchall()

    for row in rows:
        print(row)










# def main(argv):
#     if len(sys.argv) != 4:
#         sys.exit(1)

#     username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

#     try:
#         # Establish a connection to the database
#         db_connect = MySQLdb.connect(
#             host="localhost", user=username, port=3306, passwd=password, db=database
#         )

#         # Create a cursor object
#         with db_connect.cursor() as db_cursor:
#             # Execute the query
#             db_cursor.execute("SELECT * FROM states ORDER BY states.id")
#             # Fetch all rows
#             rows_selected = db_cursor.fetchall()

#             # Print the rows
#             for row in rows_selected:
#                 print(row)

#     except MySQLdb.Error as e:
#         sys.exit(1)

#     finally:
#         # Close the connection
#         if db_cursor in locals():
#             db_cursor.close()
#         if db_connect in locals():
#             db_connect.close()

# if __name__ == '__main__':
#     main(sys.argv)
