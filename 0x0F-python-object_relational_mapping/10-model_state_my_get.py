#!/usr/bin/python3
"""
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
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

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
