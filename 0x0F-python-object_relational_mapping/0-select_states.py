#!/usr/bin/python3
"""
connects to a MySQL database and lists all states from the hbtn_0e_0_usa table
"""

import MySQLdb
import sys

"""collect arguments from cmd line"""
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

"""connect to server"""
try:
    """
    connects to new server
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
    )
    cursor = db.cursor()

    """ exec querry of mysql to fetch states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    

    """show what you have fetched"""
    fetched = cursor.fetchall()
    for line in fetched:
        print(line)

    """close connection between cursor and data base"""
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("Error connecting to MySQL database:", str(e))
