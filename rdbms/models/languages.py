from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from .users import *

class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    language = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
