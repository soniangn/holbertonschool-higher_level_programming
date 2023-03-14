#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
"""
from sys import argv
import MySQLdb as DB


if __name__ == "__main__":
    db_connect = DB.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE states.name \
                        LIKE BINARY 'N%' ORDER BY states.id")
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
