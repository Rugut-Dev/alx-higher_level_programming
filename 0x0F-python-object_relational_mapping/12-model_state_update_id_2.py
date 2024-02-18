#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
