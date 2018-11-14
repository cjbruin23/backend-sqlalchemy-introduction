from sqlalchemy import Column, ForeignKey, Text, Date
from .users import *

class Employment(Base):
    __tablename__ = "employments"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    occupation = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
