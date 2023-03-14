#!/usr/bin/python3
from sqlalchemy import (create_engine)
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
""" module"""


Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:root@localhost:3306')
    
if __name__ == "__main__":
    class State(Base):
        """ class State """
        __tablename__ = 'states'
        id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)