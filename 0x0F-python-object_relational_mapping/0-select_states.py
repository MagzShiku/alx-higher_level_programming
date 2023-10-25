#!/usr/bin/python3
"""
connects to a MySQL database and lists all states from the hbtn_0e_0_usa table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """collect arguments from cmd line"""
    """connect to server"""
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
    )
    cursor = db.cursor()

    """ exec querry of mysql to fetch states"""
    cursor.execute("SELECT * FROM states")

    """Display the results"""
    for row in cursor.fetchall():
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()
