#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py that contains the
class definition of a City
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database
    """

    d_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], "password", argv[3])
    engine = create_engine(d_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    ret_val = session.query(City, State).join(State)
    for city, state in ret_val.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
