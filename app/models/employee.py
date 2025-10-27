from sqlalchemy import Column, String, Date, Integer
from app.db.base import Base  # or from app.db.session import Base if you're using declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    department = Column(String, nullable=False)
    role = Column(String, nullable=False)
    date_joined = Column(Date, nullable=False)
