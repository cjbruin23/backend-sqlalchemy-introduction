from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from .users import *

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street_address = Column(Text)
    street_address_two = Column(Text)
    city = Column(Text)
    state = Column(Text)
    postal_code = Column(Integer)
    country = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
