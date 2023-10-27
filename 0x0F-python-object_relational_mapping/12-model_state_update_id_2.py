#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Get command line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    create engine to access server
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name),
            pool_pre_ping=True)

    """
    start session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    querry the server
    """
    state = session.query(State).filter(State.id == 2).first()

    """
    change the name of state
    """
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State not found")

    """
    close session
    """
    session.close()
