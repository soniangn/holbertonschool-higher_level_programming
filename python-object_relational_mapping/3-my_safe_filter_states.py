#!/usr/bin/python3
""" takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name searched
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb as DB

    db_connect = DB.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cmd = argv[4]

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name = %(name)s \
             ORDER BY states.id", {'name': cmd})
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
