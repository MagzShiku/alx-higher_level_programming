#!/usr/bin/python3
"""
takes the state as an argument, lists things about it
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    get the arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    """
    Connect to the MySQL server
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    """
    Carry out the query in SQL
    """
    cursor = db.cursor()

    """
    Carry out query to retrieve cities of the given state
    """
    query = f"SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{state}' \
            GROUP BY states.id"
    cursor.execute(query)

    """
    fetch row
    """
    row = cursor.fetchone()

    if row is not None:
        cities = row[0]
        print(cities)

    else:
        print(f"")

    """
    Close the cursor and database connection
    """
    cursor.close()
    db.close()
