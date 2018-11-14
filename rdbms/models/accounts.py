from sqlalchemy import Column, Integer, String, ForeignKey
from .users import *

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    social_media_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

