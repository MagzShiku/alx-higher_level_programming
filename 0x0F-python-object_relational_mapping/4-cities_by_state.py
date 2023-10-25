#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Get the command-line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
    carry out the querries in SQL
    """
    cursor = db.cursor()

    """
    carry out querry to retrieve cities
    """
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    """
    fetch rows
    """
    fetched = cursor.fetchall()

    """
    show results of fetched rows
    """
    for line in fetched:
        print(line)

    """
    close the cursoe
    """
    cursor.close()
    db.close()
