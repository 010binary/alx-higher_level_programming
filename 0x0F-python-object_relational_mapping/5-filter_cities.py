#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
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
    curs.execute("SELECT * FROM `cities` as `cur` \
                INNER JOIN `states` as `st` \
                ON `cur`.`state_id` = `st`.`id` \
                ORDER BY `cur`.`id`")
    print(", ".join([cty[2] for cty in curs.fetchall() if cty[4] == argv[4]]))
