#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa

Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
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

    db_cursor = db_connect.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM states, cities \
            WHERE states.id = cities.state_id ORDER BY cities.id"
    db_cursor.execute(query)
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
