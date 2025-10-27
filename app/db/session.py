import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()  # Safe even if no .env file

DATABASE_URL = os.getenv("DATABASE_URL")

# Debug print to verify the value
print("DATABASE_URL:", repr(DATABASE_URL))

# Raise error if not set
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your Render environment variables.")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
