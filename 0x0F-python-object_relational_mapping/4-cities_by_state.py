#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""


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

    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    [print(city) for city in curs.fetchall()]
    curs.close()