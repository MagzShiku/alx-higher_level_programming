#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    get commandline args
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    create engine to connect to server
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                mysql_username, mysql_password, database_name
            ),
            pool_pre_ping=True
    )

    """
    create session factory
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    ask database for statename
    """
    state = session.query(State).filter(State.name == state_name).first()

    """
    check if state is found
    """
    if state:
        print(state.id)
    else:
        print("Not Found")
