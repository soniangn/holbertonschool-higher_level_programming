#!/usr/bin/python3
""" module that prints all City objects
from the database hbtn_0e_14_usa

Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
"""
from model_state import Base, State
from model_city import City
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

    cities = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
