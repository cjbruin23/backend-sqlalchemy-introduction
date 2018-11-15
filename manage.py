import click
from sqlalchemy.orm import sessionmaker
from mimesis import (Person, Address as Addy, Datetime, Internet)
from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models.users import *
from rdbms.models.addresses import *
from rdbms.models.accounts import *
from rdbms.models.vitals import *
from rdbms.models.education import *




@click.group()
def cli():
    pass

@cli.command()
def init():

    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)

    for _ in range(50):
        person = Person('en')
        address = Addy('en')
        date_time = Datetime('en')
        internet = Internet('en')
        
        user = User(username=person.full_name())
        user.addresses = []
        user.accounts = []
        user.vitals = []
        
        for _ in range(10):
            # Address
            new_address = Address(street_address = address.address(), 
                                  state = address.state(),
                                  country = address.country(),
                                  start_date = date_time.date(),
                                  end_date = date_time.date()
                                 )
            user.addresses.append(new_address)

            # Accounts 
            new_account = Account(social_media_url = person.social_media_profile())
            user.accounts.append(new_account)

            # Vitals
            new_vital = Vital(height = person.height(), weight = person.weight())
            user.vitals.append(new_vital)

            # Education
            new_education = Education(school = person.university())


        
        session.add(user)
    
    session.commit()

    user_query = session.query(User)
    for _row in user_query.all():
        print(_row.accounts[0].social_media_url,
              _row.vitals[1].height)

    session.close()

if __name__ == '__main__':
    cli()
