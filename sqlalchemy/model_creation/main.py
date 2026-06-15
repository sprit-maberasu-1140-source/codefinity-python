from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

# Set up the database engine
engine = create_engine("sqlite:///data.db", echo=True)  
Base = declarative_base()  # define a base class for all models

class User(Base):
    __tablename__ = "users"  # table name in the database

    id = Column(Integer, primary_key=True)  # primary key column
    username = Column(String, nullable=False, unique=True)  # username column
    age = Column(Integer)  # age column
    is_active = Column(Boolean, default=True)  # boolean column with a default value

# Create all tables defined by models
Base.metadata.create_all(engine)