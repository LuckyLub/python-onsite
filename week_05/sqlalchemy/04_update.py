'''
Update all films in the film table to a rental_duration value of 10,
in the length of the movie is more than 150.

'''

import sqlalchemy as sqa
from Documents import postgres_login as login
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://{login.username}:{login.password}@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)
update_query = sqa.update(film).values(rental_duration=10).where(film.columns.length > 150)

select_query = sqa.select([film.columns.length, film.columns.rental_duration]).where(film.columns.length > 150)

result_proxy1 = connection.execute(update_query)
result_proxy2 = connection.execute(select_query)
result_set = result_proxy2.fetchall()

pprint(result_set)
