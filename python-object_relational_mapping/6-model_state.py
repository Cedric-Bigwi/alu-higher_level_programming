#!/usr/bin/python3
"""Create the states table in the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit()
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
