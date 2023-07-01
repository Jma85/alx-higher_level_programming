#!/usr/bin/python3
"""
<<<<<<< HEAD
Lists all states from MaJay 🤭 database hbtn_0e_0_usa
=======
A script that lists all states from the database hbtn_0e_0_usa
>>>>>>> a7ab48fb07ff2fbbe9d505bc03d54454714f837f
"""
import sys
import MySQLdb

<<<<<<< HEAD
if _name_ == '_main_':
=======
if __name__ == '__main__':
>>>>>>> a7ab48fb07ff2fbbe9d505bc03d54454714f837f
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
<<<<<<< HEAD
    rows = cur.fetchall()

    for row in rows:
        print(row)
=======
    states = cur.fetchall()

    for state in states:
        print(state)
>>>>>>> a7ab48fb07ff2fbbe9d505bc03d54454714f837f
