#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    get command line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    create engine to access server
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Delete State objects with name containing 'a'
    """
    query = session.query(State).filter(State.name.like('%a%'))
    for state in query:
        session.delete(state)

    """
    commit changes and close sesh
    """
    session.commit()
    session.close()
