from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#changed the postgres password bellow due to security
DATABASE_URL = "postgresql://postgres:27101356@localhost/HotelReservation"

# The engine is the starting point of SQLAlchemy
#This object acts as a central source of connections to a particular database
engine = create_engine(DATABASE_URL)
#sessionmaker creates new SQLAlchemy Session objects
#sessions represent a workspace for your application to interact with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

