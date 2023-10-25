#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
        carry out the sql querry to fetch states starting with 'N'
        """
        cursor.execute("SELECT * FROM states WHERE name LIKE \
                'N%' ORDER BY id ASC")

        """
        show what is fetched
        """
        fetched = cursor.fetchall()
        for line in fetched:
            print(line)

        """
        close the cursor
        """
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", str(e))
