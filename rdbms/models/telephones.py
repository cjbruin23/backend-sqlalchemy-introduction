from sqlalchemy import Column, ForeignKey
from .users import *

class Telephone(Base):
    __tablename__ = "telephones"

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
