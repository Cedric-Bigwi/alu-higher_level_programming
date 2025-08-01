#!/usr/bin/python3
"""Deletes all State objects with names containing the letter 'a' from database"""

import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Use case-insensitive match for 'a' in name
    states_to_delete = session.query(State).filter(
        func.lower(State.name).like('%a%')
    ).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
