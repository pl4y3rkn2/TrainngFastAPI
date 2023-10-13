from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://nivek2:53846247618@localhost/Proyecto")
SessionLocal = sessionmaker(bind=engine)