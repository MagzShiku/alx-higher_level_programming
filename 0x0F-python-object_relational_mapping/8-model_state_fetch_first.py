#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Get the MySQL credentials from command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    we make connection string got SALAlchemy
    """
    connection_string = f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'

    """
    create engine and session
    """
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()


    """
    Query the database for the first State object
    """
    state_1 = session.query(State).order_by(State.id).first()

    if state_1 is None:
        print("Nothing")
    else:
        print(f"{state_1.id}: {state_1.name}")

    """
    close session
    """
    session.close()
