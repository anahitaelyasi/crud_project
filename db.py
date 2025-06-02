from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#changed the postgres password bellow due to security
DATABASE_URL = "postgresql://postgres:1234@localhost/HotelReservation"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

