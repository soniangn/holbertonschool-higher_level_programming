#!/usr/bin/python3
""" module for class State """
from sqlalchemy import (create_engine)
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

    
if __name__ == "__main__":
    class State(Base):
    """ class State """
        __tablename__ = 'states'
        id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)
