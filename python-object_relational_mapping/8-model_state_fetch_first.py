#!/usr/bin/python3
""" module that prints the first State object from the database hbtn_0e_6_usa
Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
"""
from model_state import Base, State
import sqlalchemy
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    Session.configure(bind=engine)

    state = session.query(State).first()

    if state:
        print("{}: {}".format(state.__dict__['id'], state.__dict__['name']))
    else:
        print("Nothing")

    session.close()
