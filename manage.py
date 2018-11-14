import click
from sqlalchemy.orm import sessionmaker
from mimesis import Person
from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models.users import *


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
        user = User(username=person.full_name())
        session.add(user)

    user_query = session.query(User)
    for _row in user_query.all():
        print(_row.username)

    session.close()

if __name__ == '__main__':
    cli()
