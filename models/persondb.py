from sqlalchemy.orm import declarative_base
from datetime import datetime 
from sqlalchemy import Column, DateTime, Integer, String
from models.sql import SessionLocal

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key = True)
    name = Column(String(20), nullable=False, unique=False)
    email = Column(String(255), nullable=False, unique=True)
    created_at =Column(DateTime(), default=datetime.now())
    
class Item(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key = True)
    name = Column(String(20), nullable=False, unique=False)
    price = Column(String(6), nullable=False, unique=False)
    created_at =Column(DateTime(), default=datetime.now())
