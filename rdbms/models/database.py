from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Echo=True allows for more robust output about database interactions
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()