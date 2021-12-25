from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# user-name: postgres
# password: admin
# database: flights_db
connection_string = 'postgresql+psycopg2://postgres:305242786@localhost/Student'

Base = declarative_base()

engine = create_engine(connection_string, echo=True)  # echo makes the console print all the sql statements being run
# con

def create_all_entities():
    Base.metadata.create_all(engine)

Session = sessionmaker()

local_session = Session(bind=engine) # cursor


