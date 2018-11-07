from sqlalchemy import Column, Integer, ForeignKey, Text
from .users import *

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    body = Column(Text())
    user_id = Column(Integer, ForeignKey(User.id))
