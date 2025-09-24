from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///data/database.sqlite")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

