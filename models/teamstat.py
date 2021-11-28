from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from models.base import Base


class TeamStat(Base):
    __tablename__ = 'teamstats'

    season = Column(Integer)
    date = Column(DateTime)
    location = Column(String(1))
    goals = Column(Integer)
    expected_goals = Column(Float)
    shots = Column(Integer)
    shots_on_target = Column(Integer)
    deep = Column(Integer)
    ppda = Column(Float)
    fouls = Column(Integer)
    corners = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    result = Column(String(1))
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer) #ForeignKey('game.id')


