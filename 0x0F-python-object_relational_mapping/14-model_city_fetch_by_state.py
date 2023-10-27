#!/usr/bin/python3
"""
contains the class definition of a City
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    get command line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    create engine
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    cerare a query
    """
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).first().name
        print(f"{state_name}: ({city.id}) {city.name}")
