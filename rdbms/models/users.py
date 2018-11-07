from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import *
from .posts import *

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    posts = relationship("Post")