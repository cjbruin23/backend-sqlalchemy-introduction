from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from .users import *

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True)
    school = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    graduated = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

