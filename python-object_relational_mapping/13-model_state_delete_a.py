#!/usr/bin/python3
"""Delete all State objects whose names contain the letter 'a' (case-insensitive)."""

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

    states_to_delete = session.query(State).filter(
        func.lower(State.name).like('%a%')
    ).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
