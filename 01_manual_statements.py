from db_config import engine
from sqlalchemy import text

with engine.connect() as connection:
    results = connection.execute(text("select * from players limit 10"))
    for player in results:
        print(player)

