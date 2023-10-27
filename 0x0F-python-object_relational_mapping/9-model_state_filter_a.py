#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    get the arguments for the command line
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    """
    Create engine to connect to MySQL server
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, dbname),
            pool_pre_ping=True)


    """
    Create a session to interact with the database
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    querry objects that start with "a"
    """
    states_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    if states_a:
        for each_state in states_a:
            print(f"{each_state.id}: {each_state.name}")
    else:
        print("Nothing")

    """
    close session
    """
    session.close()
