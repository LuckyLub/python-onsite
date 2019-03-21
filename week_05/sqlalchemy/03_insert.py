'''
Insert a new record in the film table.

'''

import sqlalchemy as sqa
from Documents import postgres_login as login
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://{login.username}:{login.password}@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)
insert_query = sqa.insert(film,
                   {"title": "CodingNomads, the Movie",
                    "description": "This is a movie on people learning how to code in Bali, when all of a sudden the "
                                   "internet dies. How wil they be able to learn when they don't have access to "
                                   "Stackoverflow or Medium?",
                    "release_year": 2019,
                    "rental_rate": 1,
                    "language_id": 1
                    })

select_query = sqa.select([film]).where(film.columns.release_year == 2019)

result_proxy1 = connection.execute(insert_query)
result_proxy2 = connection.execute(select_query)
result_set = result_proxy2.fetchall()

pprint(result_set)