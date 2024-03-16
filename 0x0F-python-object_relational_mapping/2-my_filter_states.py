#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
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

    #Executing my query
    cur = db.cursor()
