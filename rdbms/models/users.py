from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import *
from .accounts import *
from .languages import *
from .profiles import *
from .telephones import *
from .employments import *
from .education import *
from .profiles import *
from .vitals import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    addresses = relationship("Address", backref="users")
    accounts = relationship("Account", backref="users")
    languages = relationship("Language", backref="users")
    profiles = relationship("Profile", backref="users")
    education = relationship("Education", backref="users")
    employments = relationship("Employment", backref="users")
    profiles = relationship("Profile", backref="users")
    vitals = relationship("Vital", backref="users")