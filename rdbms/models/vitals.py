from sqlalchemy import Column,  Integer, ForeignKey
from .users import *

class Vital(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True)
    height = Column(String)
    weight = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
