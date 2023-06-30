#!/usr/bin/python3
"""
Lists all states from MaJay 🤭 database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if _name_ == '_main_':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()

    for row in rows:
        print(row)
