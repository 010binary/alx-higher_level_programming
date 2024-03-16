#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connecting to the db
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    # Executing my Query
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
