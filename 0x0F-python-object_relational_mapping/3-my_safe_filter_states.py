#!/usr/bin/python3
""" A script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument. safe from SQL injection
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    p = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (p, ))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
