#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    # connecting to the db
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],)

    # create cursor to exec queries using SQL
    curs = db.cursor()
    curs.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in curs.fetchall()]
    curs.close()
    db.close()
