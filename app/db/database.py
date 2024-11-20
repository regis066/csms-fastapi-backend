from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Load database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker instance (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency function to get the database session
def get_db() -> Session:
    db = SessionLocal()  # Create a new session using SessionLocal
    try:
        yield db  # Yield the session to be used in FastAPI routes
    finally:
        db.close()  # Close the session when done


# Declarative base for models
Base = declarative_base()
