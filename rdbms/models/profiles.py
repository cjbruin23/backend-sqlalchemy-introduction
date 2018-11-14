from sqlalchemy import Column, ForeignKey
from .users import *

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    nationality = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
