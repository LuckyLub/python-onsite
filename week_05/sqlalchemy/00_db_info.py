'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy as sqa
from Documents import postgres_login as login

DATABASE_URI = f'postgres+psycopg2://{login.username}:{login.password}@localhost:5432/dvdrental'
engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

category = sqa.Table('category', metadata, autoload=True, autoload_with=engine)
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)

tables = [category, film]

for table in tables:
    print(table.columns.keys())
    print(repr(metadata.tables[table.name]))





