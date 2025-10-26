from sqlalchemy import Column, String, Integer, Date, ForeignKey
from app.db.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    department = Column(String)
    date_joined = Column(Date)
