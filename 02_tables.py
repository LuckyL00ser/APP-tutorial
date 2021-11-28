from db_config import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, union_all

meta = MetaData()

coaches = Table('coaches', meta,
                Column('id', Integer, autoincrement=True, primary_key=True),
                Column('name', String(255)),
                Column('age', Integer))

# meta.create_all(engine)

with engine.begin() as connection:
    connection.execute(coaches.insert().values([
        {'name': 'Paulo Sousa', 'age': 54},
        {'name': 'Jan Kowalski', 'age': 45},
        {'name': 'Jan Smith', 'age': 34}
    ]))
    statement = union_all(coaches.select().where(coaches.c.age > 50),
                          coaches.select().where(coaches.c.name.like("%Jan%")))

    print(connection.execute(statement).fetchall())
