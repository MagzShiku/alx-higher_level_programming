#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Collect command line arguments
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to MySQL server
    """
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=mysql_user,
                passwd=mysql_password,
                db=database_name
        )
        cursor = db.cursor()

        """
        Carry out the SQL query to fetch states where name matches the argument
        """
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        """
        Show the fetched results
        """
        fetched = cursor.fetchall()
        for line in fetched:
            print(line)

        """
        Close the cursor and the database connection
        """
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", str(e))
