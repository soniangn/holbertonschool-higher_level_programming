#!/usr/bin/python3
""" module that changes the name of a State object
from the database hbtn_0e_6_usa

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

    user_query = session.query(State).filter(State.id == 2)
    data = dict(name='New Mexico')
    user_query.update(data)
    session.commit()

    session.close()
