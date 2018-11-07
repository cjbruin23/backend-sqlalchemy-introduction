from sqlalchemy import Column, Integer, ForeignKey, Text
from .users import *

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    body = Column(Text())
    user_id = Column(Integer, ForeignKey(User.id))
