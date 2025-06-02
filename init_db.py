from db import Base, engine 
from models import * 

# This will create the tables in the PostgreSQL DB
Base.metadata.create_all(bind=engine)
