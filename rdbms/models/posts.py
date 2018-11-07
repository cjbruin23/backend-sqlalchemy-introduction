from sqlalchemy import Column, Integer, String, ForeignKey, Text
from .users import *

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    title = Column(String(255))
    body = Column(Text())
    user_id = Column(Integer, ForeignKey(User.id))
