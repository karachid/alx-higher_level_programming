#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa
    grouping by states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM
                states s, cities c WHERE c.state_id=s.id""")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
