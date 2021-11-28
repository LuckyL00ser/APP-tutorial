import time

from sqlalchemy import text, select, and_
from sqlalchemy.orm import sessionmaker, joinedload, lazyload, subqueryload, selectinload, raiseload

from db_config import engine
from models.base import Base

from models.game import Game
from models.league import League
from models.team import Team

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
# 1
# session.add_all([
#     League(name="Ekstraklasa"),
#     League(name="A Class"),
#     League(name="B Class")
# ])
# session.commit()

# 2
# print(session.query(League).filter(text("id>5")).all())

# 3
# how many home games teams from Manchester won in Premier League in 2015 season?
# result = session.query(Game)\
#     .join(Game.home_team)\
#     .join(Game.league)\
#     .filter(
#             Team.name.like("Manchester%"),
#             League.name == "Premier League",
#             Game.season==2015,
#             Game.home_goals > Game.away_goals)\
#     .count()
# print(result)

#4 lazy loading
t = time.process_time()
result = session.query(Game).limit(5000).all()
for game in result:
    game.home_team

print(f"Time elapsed = {time.process_time() - t}")

t = time.process_time()
result = session.query(Game).options(joinedload(Game.home_team)).limit(5000).all()
for game in result:
    game.home_team
print(f"Time elapsed after eager load = {time.process_time() - t}")

