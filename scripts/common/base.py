# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session#, declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Create the engine
engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/dwh")

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()