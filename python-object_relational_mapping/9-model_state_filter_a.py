"""Script to list all State objects containing the letter 'a' from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1:]

    # Connect to MySQL server using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    
    # Create a session
    session = Session(engine)

    # Query State objects containing the letter 'a' and print the results
    states_with_a = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()