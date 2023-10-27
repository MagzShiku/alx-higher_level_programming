#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    get the command line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    create engine to 
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name))

    """
    create sessoin
    """
    Session = sessionmaker(bind=engine)

    session = Session()

    """
    Create a new State object
    """
    new_state = State(name="Louisiana")

    """
    Add the new State object to the session
    """
    session.add(new_state)
    session.commit()

    """
    return the new state id
    """
    print(new_state.id)
