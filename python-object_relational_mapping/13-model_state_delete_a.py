#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete all the matching states
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to persist changes in the database
    session.commit()

    # Close session
    session.close()

